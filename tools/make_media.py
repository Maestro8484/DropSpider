"""Photos and video into the README from one drop folder.

The originals stay outside the project, in

    C:\\Users\\SuperMaster\\Documents\\_Projects\\Projects-Media-Photos-Docs\\DropSpider\\

Drop phone photos and clips there, any names, any order, then double-click scripts\\add_photos.bat
(which runs this). Each run:

  photos (.jpg .jpeg .png)   -> media/porch_01.jpg, porch_02.jpg ... in the order they were taken (EXIF date,
                                else the file's date), 1600 px on the long side, about 300 KB, turned the right
                                way up, every bit of EXIF (GPS included) stripped. A photo keeps its number for
                                good: media/sources.txt remembers which original became which porch_NN.
  media/captions.txt         -> one line per picture, "porch_01.jpg: caption". A new picture gets a placeholder
                                line; a line you have edited is never touched. Edit it, run again.
  clips (.mp4 .mov)          -> media/clip_01.mp4 ... Over 20 s or over 10 MB: a 10 s copy from the start,
                                720 px tall, made with ffmpeg if it is on this PC (else the clip is left and the
                                run says so). A poster picture (the first frame) beside each clip.
  media/youtube.txt          -> if the drop folder holds youtube.txt with a YouTube or Shorts link, its thumbnail
                                is fetched to media/youtube.jpg and the README's top shows it as a clickable picture.
  README.md                  -> rewritten between <!-- video:start --> / <!-- video:end --> (the top slot: the
                                YouTube picture, else the first clip's poster linked to the clip) and between
                                <!-- media:start --> / <!-- media:end --> (the photos with their captions).
  media/video.txt            -> the one step this script cannot do: GitHub plays a clip inside a README only when
                                the file is dragged into the README on github.com while editing (a clip in the
                                project is a link, not a player). The .txt says exactly what to drag and where.

    python tools/make_media.py            do all of the above (writes only what changed)
    python tools/make_media.py --check    exit 1 if the README slots are stale (passes when the drop folder is absent)
    python tools/make_media.py --redo     remake every picture and clip even if it exists

Needs Pillow. HEIC photos need the pillow-heif package; without it they are listed and skipped.
"""
import io
import os
import re
import shutil
import subprocess
import sys
import urllib.request

from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = r"C:\Users\SuperMaster\Documents\_Projects\Projects-Media-Photos-Docs\DropSpider"
MEDIA = os.path.join(ROOT, "media")
README = os.path.join(ROOT, "README.md")
SOURCES = os.path.join(MEDIA, "sources.txt")
CAPTIONS = os.path.join(MEDIA, "captions.txt")
VIDEO_TXT = os.path.join(MEDIA, "video.txt")
PHOTO_EXT = (".jpg", ".jpeg", ".png", ".heic")
CLIP_EXT = (".mp4", ".mov")
LONG_SIDE = 1600
TARGET_KB = 300
CLIP_MAX_S = 20
CLIP_MAX_MB = 10
PLACEHOLDER = "the device on the porch (edit this line in media/captions.txt)"

try:
    import pillow_heif  # noqa: F401
    pillow_heif.register_heif_opener()
    HEIC = True
except ImportError:
    HEIC = False


def read_pairs(path):
    """'key: value' lines (or 'key <- value' in sources.txt) into an ordered dict; '#' lines kept aside."""
    out = {}
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^(\S+)\s*(?::|<-)\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def write_if_changed(path, text):
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old != text:
        open(path, "w", encoding="utf-8", newline="\n").write(text)
        return True
    return False


def taken(path):
    """EXIF DateTimeOriginal as a sortable string, else the file's modified time."""
    try:
        with Image.open(path) as im:
            exif = im.getexif()
            d = exif.get(36867) or exif.get(306)
            if d:
                return str(d)
    except Exception:
        pass
    return "%015.3f" % os.path.getmtime(path)


def ffprobe_seconds(path):
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                           capture_output=True, text=True, timeout=60)
        return float(r.stdout.strip())
    except Exception:
        return None


def have(tool):
    return shutil.which(tool) is not None


def make_photo(src, dst):
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        if max(im.size) > LONG_SIDE:
            s = LONG_SIDE / max(im.size)
            im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        q = 85
        while True:
            buf = io.BytesIO()
            im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)   # no exif argument: nothing carried over
            if buf.tell() <= TARGET_KB * 1024 * 1.15 or q <= 60:
                break
            q -= 5
    open(dst, "wb").write(buf.getvalue())
    return buf.tell() // 1024


def make_clip(src, dst, poster):
    """Copy the clip (trimmed with ffmpeg if long or big) and write its first frame as a poster. Returns a note."""
    size_mb = os.path.getsize(src) / 1e6
    secs = ffprobe_seconds(src) if have("ffprobe") else None
    long = (secs is not None and secs > CLIP_MAX_S) or size_mb > CLIP_MAX_MB
    note = ""
    if long and have("ffmpeg"):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src, "-t", str(10), "-vf", "scale=-2:720", "-c:v", "libx264",
                        "-preset", "medium", "-crf", "28", "-an", "-movflags", "+faststart", dst], check=True, timeout=600)
        note = "re-encoded at 720 px, first 10 s at most (the original is %.0f s, %.1f MB)" % (secs or 0, size_mb)
    elif long:
        shutil.copyfile(src, dst)
        note = "copied as is: %.1f MB, %s; ffmpeg is not on this PC, so no trimmed copy" % (size_mb, ("%.0f s" % secs) if secs else "length unknown")
    else:
        shutil.copyfile(src, dst)
        note = "copied as is (%.1f MB)" % size_mb
    if have("ffmpeg"):
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", dst, "-frames:v", "1", "-vf", "scale=-2:720", "-q:v", "4", poster],
                       check=False, timeout=120)
    return note


def youtube_id(text):
    m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/)([A-Za-z0-9_-]{11})", text)
    return m.group(1) if m else None


def fetch_thumb(vid, dst):
    for name in ("maxresdefault.jpg", "hqdefault.jpg"):
        try:
            data = urllib.request.urlopen("https://img.youtube.com/vi/%s/%s" % (vid, name), timeout=20).read()
            if len(data) > 2000:
                open(dst, "wb").write(data)
                return name
        except Exception:
            continue
    return None


def splice(text, name, body):
    start, end = "<!-- " + name + ":start -->", "<!-- " + name + ":end -->"
    if start not in text or end not in text:
        return None
    a = text.index(start) + len(start)
    b = text.index(end)
    return text[:a] + "\n" + body + ("\n" if body else "") + text[b:]


def main():
    check = "--check" in sys.argv
    redo = "--redo" in sys.argv
    if not os.path.isdir(SRC):
        if check:
            print("media: drop folder not on this PC, nothing to check")
            return
        os.makedirs(SRC, exist_ok=True)
        print("made the drop folder: " + SRC)
        print("drop phone photos and clips in it, then run this again")
        return
    os.makedirs(MEDIA, exist_ok=True)
    changed = []

    files = sorted(os.listdir(SRC))
    photos = [f for f in files if f.lower().endswith(PHOTO_EXT)]
    clips = [f for f in files if f.lower().endswith(CLIP_EXT)]
    yt = [f for f in files if f.lower() == "youtube.txt"]

    # which original became which porch_NN: numbers never change once given
    sources = read_pairs(SOURCES)          # porch_01.jpg -> original name
    by_source = {v: k for k, v in sources.items()}
    new_photos = [f for f in photos if f not in by_source]
    new_photos.sort(key=lambda f: taken(os.path.join(SRC, f)))
    next_n = max([int(m.group(1)) for k in sources for m in [re.match(r"porch_(\d+)\.jpg", k)] if m] + [0]) + 1
    for f in new_photos:
        name = "porch_%02d.jpg" % next_n
        next_n += 1
        sources[name] = f
        by_source[f] = name

    skipped = []
    for name, f in sorted(sources.items()):
        src = os.path.join(SRC, f)
        dst = os.path.join(MEDIA, name)
        if not os.path.exists(src):
            continue  # the original is gone; the copy already made stays
        if f.lower().endswith(".heic") and not HEIC:
            skipped.append(f)
            continue
        if redo or not os.path.exists(dst):
            if check:
                changed.append(name)
                continue
            kb = make_photo(src, dst)
            changed.append("%s (%d KB, from %s)" % (name, kb, f))

    # clips
    clip_names = {}
    clip_notes = {}
    for i, f in enumerate(sorted(clips, key=lambda f: taken(os.path.join(SRC, f))), 1):
        name = "clip_%02d.mp4" % i
        poster = "clip_%02d.jpg" % i
        sources.setdefault(name, f)
        clip_names[name] = poster
        dst = os.path.join(MEDIA, name)
        if redo or not os.path.exists(dst):
            if check:
                changed.append(name)
                continue
            clip_notes[name] = make_clip(os.path.join(SRC, f), dst, os.path.join(MEDIA, poster))
            changed.append("%s (%s, from %s)" % (name, clip_notes[name], f))

    # youtube
    yt_url, yt_thumb = None, None
    if yt:
        text = open(os.path.join(SRC, yt[0]), encoding="utf-8", errors="replace").read()
        vid = youtube_id(text)
        if vid:
            yt_url = "https://www.youtube.com/watch?v=" + vid
            yt_thumb = os.path.join(MEDIA, "youtube.jpg")
            if (redo or not os.path.exists(yt_thumb)) and not check:
                got = fetch_thumb(vid, yt_thumb)
                changed.append("youtube.jpg (%s)" % got if got else "youtube.jpg NOT fetched")
        else:
            print("youtube.txt has no YouTube link I can read")

    if not check:
        lines = ["# which original in the drop folder became which file here. Made by tools/make_media.py; a number never changes."]
        lines += ["%s <- %s" % (k, v) for k, v in sorted(sources.items())]
        if write_if_changed(SOURCES, "\n".join(lines) + "\n"):
            changed.append("sources.txt")

    # captions: add a placeholder line per new picture, never touch an existing line
    captions = read_pairs(CAPTIONS)
    cap_lines = open(CAPTIONS, encoding="utf-8").read().splitlines() if os.path.exists(CAPTIONS) else [
        "# One line per picture: file name, colon, the caption that shows under it in the README. Edit the words, run add_photos.bat again."]
    for name in sorted(k for k in sources if k.startswith("porch_")):
        if name not in captions and os.path.exists(os.path.join(MEDIA, name)):
            cap_lines.append("%s: %s" % (name, PLACEHOLDER))
            captions[name] = PLACEHOLDER
    if not check and write_if_changed(CAPTIONS, "\n".join(cap_lines) + "\n"):
        changed.append("captions.txt")

    # README slots
    top = []
    first_clip = sorted(clip_names)[0] if clip_names else None
    if yt_url and yt_thumb and os.path.exists(yt_thumb):
        top.append("[![Watch the spider drop (YouTube)](media/youtube.jpg)](%s)" % yt_url)
    elif first_clip and os.path.exists(os.path.join(MEDIA, clip_names[first_clip])):
        top.append("[![The spider dropping; click for the clip](media/%s)](media/%s)" % (clip_names[first_clip], first_clip))
        top.append("")
        top.append("*Click the picture for the clip (mp4).*")
    gallery = []
    for name in sorted(k for k in sources if k.startswith("porch_") and os.path.exists(os.path.join(MEDIA, k))):
        cap = captions.get(name, PLACEHOLDER)
        gallery.append("![%s](media/%s)" % (cap.replace("]", ")"), name))
        gallery.append("")
        gallery.append("*%s*" % cap)
        gallery.append("")
    for name in sorted(clip_names)[1:] if yt_url else sorted(clip_names)[1:]:
        gallery.append("- [Another clip](media/%s) (mp4)" % name)
    if gallery and gallery[-1] == "":
        gallery.pop()

    readme = open(README, encoding="utf-8").read()
    new = splice(readme, "video", "\n".join(top))
    new = splice(new if new is not None else readme, "media", "\n".join(gallery))
    if new is None:
        print("README.md is missing a <!-- video --> or <!-- media --> slot; README not touched")
    elif new != readme:
        changed.append("README.md")
        if not check:
            open(README, "w", encoding="utf-8", newline="\n").write(new)

    # video.txt: the one hand step
    if not check:
        if clip_names:
            vt = ["The clip is in the project as media/%s (the run that made it said whether it was trimmed)." % first_clip,
                  "",
                  "GitHub only PLAYS a video inside the README when the file is dragged in while editing on github.com.",
                  "A clip sitting in the project shows as a link, which the README already has.",
                  "To get the player, once, by hand:",
                  "  1. Open https://github.com/Maestro8484/DropSpider/edit/master/README.md in Chrome (signed in).",
                  "  2. Click on the empty line right under the line  <!-- video:start -->  near the top.",
                  "  3. Drag %s from this media folder into the editor. GitHub uploads it and writes a link ending in .mp4 (or a user-attachments address)." % first_clip,
                  "  4. Commit changes (the green button). Done: the README plays the clip.",
                  "A YouTube link does the same job with no upload: put it in youtube.txt in the drop folder and run add_photos.bat."]
        else:
            vt = ["No clip in the drop folder yet. Drop an .mp4 or .mov there and run add_photos.bat."]
        if write_if_changed(VIDEO_TXT, "\n".join(vt) + "\n"):
            changed.append("video.txt")

    if skipped:
        print("skipped (HEIC needs the pillow-heif package: pip install pillow-heif): " + ", ".join(skipped))
    if check:
        if changed:
            print("STALE: " + ", ".join(changed) + " (run scripts/add_photos.bat)")
            sys.exit(1)
        print("media matches the drop folder")
    else:
        print(("wrote " + ", ".join(changed)) if changed else "nothing changed")
        print("%d photos, %d clips%s in %s" % (len(photos), len(clips), ", a YouTube link" if yt_url else "", SRC))


if __name__ == "__main__":
    main()
