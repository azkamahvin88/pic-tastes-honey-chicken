# Honey-Glazed Fried Chicken — The Picture That Tastes of One Ingredient

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)

One picture of food, judged on how delicious it looks. This entry is a single
photorealistic close-up of honey-glazed fried chicken: steaming, crispy,
glaze dripping, filling the whole frame against a dark background. One hero
ingredient, nothing else competing for the eye.

## Program

`main.py` (Python 3.13, standard library only, no network) copies the entry
image to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). The image
is a 1024×683 PNG of 999,080 bytes, well under the 1 MiB / 1024×1024 limits,
so every run produces identical bytes.

Run it with:

```sh
python3 main.py
```
