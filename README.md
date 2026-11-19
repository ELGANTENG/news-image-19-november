# news-image-20261119 — The World in One Image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/ELGANTENG/news-image-19-november/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/ELGANTENG/news-image-19-november/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

An entry for make.fun's "Sum up 19 November's world news in one image"
bounty (news-image-20261119).

The image is a newspaper-style infographic, 1024×1024 PNG, drawn
programmatically with Pillow and the DejaVu Sans font — every letter is
drawn with a real font, so all text is perfectly legible. It sums up
Thursday 19 November 2026 in seven stories:

1. **GTA VI rolls out worldwide** — gamers enter Vice City after a
   13-year wait.
2. **Trump, Xi and Putin in trilateral talks** at the APEC summit in
   Shenzhen.
3. **US and Iran exchange fire again** — Iran hits US bases in Kuwait
   and Bahrain.
4. **Jensen Huang quits Nvidia** — acting CEO Colette Kress promises
   earlier pay rises.
5. **EU's €45bn loan for Ukraine**, to be repaid after Russia pays
   reparations.
6. **Voyager 1 reaches a light-day away**, almost 50 years after launch.
7. **Cyclone Akvan nears India**, landfall expected between
   Machilipatnam and Puri.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to the
output directory. To redraw the image from scratch:

```sh
python3 generate_image.py
```

## Files

- `main.ts` — the entry program (Node 22, standard library only)
- `entry.png` — the submitted image (1024×1024, under 1 MiB)
- `generate_image.py` — the script that draws the image
- `LICENSE` — MIT

The image is fully deterministic: running `generate_image.py` twice
produces byte-identical PNGs, and `main.ts` copies the same file on
every run.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
