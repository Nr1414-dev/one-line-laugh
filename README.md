# The One-Line Laugh

[![make.fun bounty](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Nr1414-dev/one-line-laugh/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Nr1414-dev/one-line-laugh/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for the [make.fun](https://make.fun) bounty
["The One-Line Laugh"](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f).

## The line

> My phone autocorrected 'I'll be there in five minutes' to 'I'll be there in five hours' — for once, it told the truth.

## Why this line

- One funny line, one sentence, 118 characters — inside the 200-character cap.
- Surprise at the end: autocorrect, famous for mangling what we meant,
  accidentally tells the truth — the turn lands after the em-dash and
  still makes sense once it arrives.
- Everyday truth: "I'll be there in five minutes" is the small lie
  everyone tells, and autocorrect mishaps are universal.
- Economical: every word earns its place, nothing explains the joke.
- Fresh angle: the joke is not that autocorrect got it wrong, but that
  for once it got it right.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (UTF-8, no trailing newline,
118 characters). The program validates the text is 1–200 Unicode code
points before writing. Set `ENTRY_OUTPUT_DIR` to write elsewhere.

## Verification

Deterministic output: running `main.py` twice to different directories
produces byte-identical `entry.txt` files (same SHA-256). The committed
`entry.txt` matches that hash as well.

## License

MIT — see [LICENSE](LICENSE).
