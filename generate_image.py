#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news infographic, 1024x1024 PNG.

Every letter is drawn with a real font (DejaVu Sans), so all text stays
perfectly legible. The output is fully deterministic: same input, same
bytes, every run. Only the Python standard library and Pillow are used,
and only at build time -- the submitted entry (main.ts + entry.png)
needs nothing but Node's standard library.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
NAVY = (10, 17, 40)
PANEL = (22, 35, 63)
PANEL_EDGE = (48, 68, 110)
WHITE = (245, 247, 250)
MUTED = (176, 190, 212)
GOLD = (255, 196, 66)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(draw, x, y, text, fnt, fill, max_w, leading):
    """Draw wrapped text; returns the y just below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                           outline=outline, width=width)


def draw_header(draw):
    draw.text((24, 26), "19 NOVEMBER 2026", font=font(BOLD, 48), fill=WHITE)
    draw.text((24, 86), "THE WORLD IN ONE IMAGE",
              font=font(BOLD, 26), fill=GOLD)
    draw.text((24, 122), "THURSDAY",
              font=font(BOLD, 18), fill=MUTED)
    draw.line([(700, 44), (1000, 44)], fill=GOLD, width=4)
    draw.text((700, 56), "SEVEN STORIES", font=font(BOLD, 24), fill=WHITE)
    draw.text((700, 88), "ONE DAY", font=font(REG, 20), fill=MUTED)


def draw_hero(draw):
    """Full-width hero panel: GTA VI begins its global rollout."""
    x, y, w, h = 24, 158, 976, 204
    rounded(draw, (x, y, x + w, y + h), 18, (30, 16, 64),
            outline=(90, 60, 160), width=2)
    # Neon sunset: orange sun over a dark Vice City skyline.
    draw.ellipse([x + w - 250, y + 14, x + w - 70, y + 194],
                 fill=(255, 122, 26))
    draw.ellipse([x + w - 232, y + 32, x + w - 88, y + 176],
                 fill=(255, 196, 66))
    for bx, bh in [(0, 70), (48, 110), (96, 84), (144, 128), (192, 92)]:
        draw.rectangle([x + w - 330 + bx, y + h - bh,
                        x + w - 330 + bx + 40, y + h], fill=(16, 10, 40))
    draw.text((x + 28, y + 16), "GAMING  ·  WORLDWIDE",
              font=font(BOLD, 20), fill=(255, 122, 26))
    draw.text((x + 28, y + 46), "GTA VI ROLLS OUT",
              font=font(BOLD, 44), fill=WHITE)
    draw.text((x + 28, y + 94), "WORLDWIDE",
              font=font(BOLD, 44), fill=WHITE)
    draw.text((x + 28, y + 158), "Gamers enter Vice City after a 13-year wait.",
              font=font(REG, 23), fill=MUTED)


def icon_apec(draw, ox, oy):
    """Three overlapping circles: three leaders, one table."""
    draw.ellipse([ox, oy + 18, ox + 52, oy + 70], fill=(200, 40, 40))
    draw.ellipse([ox + 30, oy + 18, ox + 82, oy + 70], fill=(40, 90, 200))
    draw.ellipse([ox + 15, oy, ox + 67, oy + 52], fill=(245, 247, 250))
    draw.ellipse([ox + 30, oy + 15, ox + 52, oy + 37], fill=(255, 196, 66))


def icon_conflict(draw, ox, oy):
    """A globe with a red burst: strikes across the Gulf."""
    draw.ellipse([ox + 8, oy + 8, ox + 74, oy + 74], fill=(40, 90, 160))
    draw.ellipse([ox + 8, oy + 8, ox + 74, oy + 74],
                 outline=(140, 190, 255), width=2)
    draw.arc([ox + 24, oy + 8, ox + 58, oy + 74], 270, 90,
             fill=(140, 190, 255), width=2)
    draw.line([ox + 41, oy + 8, ox + 41, oy + 74], fill=(140, 190, 255),
              width=2)
    for dx, dy in [(0, -26), (24, -10), (-24, -10), (14, 22), (-14, 22)]:
        draw.line([ox + 41, oy + 41, ox + 41 + dx, oy + 41 + dy],
                  fill=(255, 70, 50), width=4)


def icon_chip(draw, ox, oy):
    """A green processor chip: Nvidia's leadership change."""
    draw.rounded_rectangle([ox + 14, oy + 14, ox + 68, oy + 68], radius=8,
                           fill=(118, 185, 0))
    draw.rounded_rectangle([ox + 26, oy + 26, ox + 56, oy + 56], radius=4,
                           fill=(30, 60, 0))
    draw.text((ox + 31, oy + 30), "NV", font=font(BOLD, 20), fill=WHITE)
    for px in (22, 41, 60):
        draw.line([ox + px, oy + 2, ox + px, oy + 14], fill=(118, 185, 0),
                  width=4)
        draw.line([ox + px, oy + 68, ox + px, oy + 80], fill=(118, 185, 0),
                  width=4)
        draw.line([ox + 2, oy + px, ox + 14, oy + px], fill=(118, 185, 0),
                  width=4)
        draw.line([ox + 68, oy + px, ox + 80, oy + px], fill=(118, 185, 0),
                  width=4)


def draw_panel(draw, x, y, w, h, kicker, headline, sub, accent, icon,
               extra=None):
    """Panel layout: icon top-right, kicker under it, headline and sub
    full-width below the icon so no text ever runs under an icon or
    past the panel's bottom edge."""
    rounded(draw, (x, y, x + w, y + h), 16, PANEL,
            outline=PANEL_EDGE, width=2)
    draw.rectangle([x + 16, y + 12, x + w - 16, y + 18], fill=accent)
    icon(draw, x + w - 100, y + 24)
    draw.text((x + 18, y + 40), kicker, font=font(BOLD, 16), fill=accent)
    yy = draw_text_block(draw, x + 18, y + 112, headline, font(BOLD, 25),
                         WHITE, w - 36, 29)
    draw_text_block(draw, x + 18, yy + 8, sub, font(REG, 18), MUTED,
                    w - 36, 23)


GRID = [
    ("DIPLOMACY",
     "Trump, Xi and Putin in trilateral talks",
     "Three leaders meet at the APEC summit in Shenzhen.",
     (255, 196, 66), icon_apec, None),
    ("MIDDLE EAST",
     "US and Iran exchange fire again",
     "Iran hits US bases in Kuwait and Bahrain.",
     (255, 70, 50), icon_conflict, None),
    ("TECH  ·  MARKETS",
     "Jensen Huang quits Nvidia",
     "Acting CEO Colette Kress promises earlier pay rises.",
     (118, 185, 0), icon_chip, None),
]


def icon_eu(draw, ox, oy):
    """EU circle of stars over Ukraine's blue and yellow."""
    draw.rectangle([ox + 8, oy + 8, ox + 74, oy + 41], fill=(0, 70, 173))
    draw.rectangle([ox + 8, oy + 41, ox + 74, oy + 74], fill=(255, 213, 0))
    import math
    for i in range(12):
        a = math.pi * 2 * i / 12 - math.pi / 2
        sx = ox + 41 + int(22 * math.cos(a))
        sy = oy + 41 + int(22 * math.sin(a))
        draw.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 213, 0))


def icon_voyager(draw, ox, oy):
    """A probe on a dotted path, a light-day from home."""
    import math
    for i in range(9):
        px = ox + 6 + i * 8
        py = oy + 66 - int(6 * math.sin(i * 0.7))
        draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=GOLD)
    draw.polygon([(ox + 62, oy + 10), (ox + 78, oy + 34), (ox + 52, oy + 34)],
                 fill=WHITE)
    draw.rectangle([ox + 58, oy + 34, ox + 66, oy + 48], fill=WHITE)
    draw.ellipse([ox + 4, oy + 6, ox + 12, oy + 14], fill=(255, 196, 66))
    draw.ellipse([ox + 70, oy + 58, ox + 78, oy + 66], fill=MUTED)


def icon_cyclone(draw, ox, oy):
    """A spiral storm over the coast."""
    for r, start in [(34, 0), (26, 60), (18, 120), (10, 180)]:
        draw.arc([ox + 41 - r, oy + 41 - r, ox + 41 + r, oy + 41 + r],
                 start, start + 270, fill=(64, 200, 220), width=5)
    draw.ellipse([ox + 36, oy + 36, ox + 46, oy + 46], fill=(64, 200, 220))


GRID2 = [
    ("EUROPE",
     "EU's €45bn loan for Ukraine",
     "To be repaid after Russia pays reparations.",
     (255, 213, 0), icon_eu, None),
    ("SPACE",
     "Voyager 1 reaches a light-day away",
     "Almost 50 years after launch, the probe keeps going.",
     (255, 196, 66), icon_voyager, None),
    ("WEATHER  ·  INDIA",
     "Cyclone Akvan nears India",
     "Landfall expected between Machilipatnam and Puri.",
     (64, 200, 220), icon_cyclone, None),
]


def main():
    img = Image.new("RGB", (W, H), NAVY)
    draw = ImageDraw.Draw(img)
    draw_header(draw)
    draw_hero(draw)
    col_w, gap = 317, 12
    for i, story in enumerate(GRID):
        x = 24 + i * (col_w + gap)
        draw_panel(draw, x, 374, col_w, 250, *story)
    for i, story in enumerate(GRID2):
        x = 24 + i * (col_w + gap)
        draw_panel(draw, x, 636, col_w, 250, *story)
    draw.line([(24, 902), (1000, 902)], fill=PANEL_EDGE, width=2)
    draw.text((24, 916), "All events of Thursday 19 November 2026",
              font=font(BOLD, 22), fill=WHITE)
    draw.text((24, 946), "One day, seven stories — as reported.",
              font=font(REG, 18), fill=MUTED)
    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
