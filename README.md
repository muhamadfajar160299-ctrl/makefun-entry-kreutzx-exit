# The One-Line Exit — Roomba Replacement

[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/muhamadfajar160299-ctrl/makefun-entry-kreutzx-exit/rank.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/muhamadfajar160299-ctrl/makefun-entry-kreutzx-exit/reward.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)

Entry for [The One-Line Exit](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
on [make.fun](https://make.fun): the funniest single-line resignation letter wins.

## The line

> Dear boss, I resign: HR asked me to train my replacement, and it turns out my replacement is a Roomba with better benefits.

One line, 123 characters. An office worker's resignation with a surprise
twist: the replacement isn't a person — it's a robot vacuum, and it gets
better benefits than the human did.

## How it runs

`main.py` (Python 3, standard library only) copies the shipped `entry.txt`
byte-identical into `$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`,
using a direct write (no temporary file):

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — entrypoint: copies `entry.txt` to the output directory.
- `entry.txt` — the one-line resignation letter (123 bytes, no trailing newline).
- `LICENSE` — MIT.
