---
name: transcribe-video
description: Transcribe a YouTube or public Facebook video to a primary-source transcript for fact-checking. Trigger when a claim hinges on what someone actually said on video, when the user drops a YouTube/Facebook video or reel URL, or says "transcribe this", "pull the transcript", "what did he actually say in the video". Produces a saved transcript under research/transcripts/ so quotes are verified from primary audio, not news paraphrase.
---

# /transcribe-video

News outlets paraphrase. For any fact-check that turns on what a person *said*
on camera, quote from the primary audio, not a secondary summary — this is
Pre-Publish Failure Mode #1 (tool/news summaries treated as primary quotes).
This command pulls the video's own transcript and saves it as a citable
artifact.

**Why it earns its place:** transcribing the source video repeatedly beats the
news coverage. The July 2026 Nick Shirley entry only exists because the
transcript showed the video *opens* naming "Korean and Chinese mafias" and 40
minutes later says it has "nothing to do with Koreans" — a self-contradiction
no outlet reported. The BUSES entry's sharpest finding ("one city's extreme
policies" undercut by his own four-state list) came straight from the committee
video's audio.

## YouTube — `youtube-transcript-api` (uses YouTube's own captions)

```python
from youtube_transcript_api import YouTubeTranscriptApi
t = YouTubeTranscriptApi().fetch("VIDEO_ID")          # the v= id
text = " ".join(s.text for s in t)
```

Installed `--user` for Python 3.9; if the import fails:
`python3 -m pip install --user youtube-transcript-api` (PATH:
`~/Library/Python/3.9/bin`). Do **not** hand-copy a signed `timedtext` URL and
curl it — those expire and return empty; use the library.

## Facebook (public reels/posts — NO login needed)

```bash
yt-dlp --no-update -f "ba[ext=m4a]/ba" -o "out.%(ext)s" "https://www.facebook.com/reel/<ID>/"
whisper out.m4a --model base.en --language en --output_format txt --fp16 False
```

`yt-dlp`, `ffmpeg`, `whisper` (openai) are brew-installed; the `base.en` model
is cached at `~/.cache/whisper/base.en.pt` (no download). Run `yt-dlp -F <url>`
first if you want to see formats. Works for `/reel/<id>/`, `/watch/?v=<id>`,
and `/<page>/posts/<id>` public URLs.

## Save the transcript (so "full transcript on file" is true)

Persist under `research/transcripts/` — it is outside `content/`, so Hugo does
not publish it, and it makes the entry's citation real:

```
research/transcripts/YYYY-MM-DD-slug_<yt-VIDEOID | fb-reel-REELID>.txt
```

## Caveats to carry into the entry

- **Whisper mishears proper nouns.** Mark reconstructions in brackets
  (`grow like [vermin]`) and, when a garble matters, corroborate the word
  against a secondary source (the raw caption read "Burman"; TAG24 confirmed
  "vermin").
- **Add a one-line methodology note** to the entry: quotes verified against the
  video's own auto-captions, pulled programmatically on <date>; transcript on
  file.
- **Cite the transcript in Sources**, and mark which Facts rest on it.
- A verbatim block quote from the transcript is stronger than any paraphrase —
  prefer it for the Statement and for the load-bearing Facts.

## Related

- `/ny23-fact-check` — the transcript feeds the draft.
- `/fact-check-review`, `/tier-a-confirm` — Failure Mode #1 is exactly what this
  pre-empts.
- Memory: `video-transcription-workflow` (machine-level note of the same flow).
