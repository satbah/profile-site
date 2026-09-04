#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate a simple placeholder illustration for the TTS/lip-sync work
card (assets/work-tts-avatar.webp), in the same dark-UI style family as
the other card thumbnails, until a proper illustration replaces it.
"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1279, 720
BG = (5, 9, 18)
LINE = (60, 90, 130)
LINE_DIM = (35, 55, 80)
CYAN = (140, 200, 230)
WARM = (255, 184, 112)
DIM = (110, 140, 165)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def font(size, bold=False):
    names = (
        ["/System/Library/Fonts/Supplemental/Arial Bold.ttf"] if bold else
        ["/System/Library/Fonts/Supplemental/Arial.ttf"]
    )
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except Exception:
            continue
    return ImageFont.load_default()


f_title = font(40, bold=True)
f_sub = font(16)
f_label = font(13)
f_mono = font(12)

# subtle grid
for x in range(0, W, 40):
    d.line([(x, 0), (x, H)], fill=(10, 16, 28), width=1)
for y in range(0, H, 40):
    d.line([(0, y), (W, y)], fill=(10, 16, 28), width=1)

# title block, top-left (matches other cards' editorial style)
d.text((50, 60), "AZURE TTS", font=f_sub, fill=WARM)
d.text((50, 85), "AVATAR LIPSYNC", font=f_title, fill=(230, 240, 248))
d.text((50, 140), "MCP  ->  SPEECH  ->  VRM VISEME", font=f_sub, fill=DIM)
d.line([(50, 170), (330, 170)], fill=LINE, width=1)

# simple "avatar head" — circle + jaw wedge suggesting a talking face
cx, cy, r = 820, 360, 190
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=CYAN, width=2)
for ang in range(0, 360, 18):
    a = math.radians(ang)
    x1, y1 = cx + math.cos(a) * (r - 6), cy + math.sin(a) * (r - 6)
    x2, y2 = cx + math.cos(a) * r, cy + math.sin(a) * r
    d.line([(x1, y1), (x2, y2)], fill=LINE_DIM, width=1)
# mouth: an open arc to suggest speech / viseme
mouth_w, mouth_h = 70, 34
d.arc([cx - mouth_w, cy + 40, cx + mouth_w, cy + 40 + mouth_h * 2],
      start=20, end=160, fill=WARM, width=4)

# waveform strip along the bottom, under the head, suggesting TTS audio
wf_y = 590
d.line([(80, wf_y), (1200, wf_y)], fill=LINE_DIM, width=1)
import random
random.seed(7)
x = 100
while x < 1180:
    h = random.randint(4, 46)
    color = WARM if random.random() < 0.18 else CYAN
    d.line([(x, wf_y - h), (x, wf_y + h)], fill=color, width=2)
    x += 6

# right-side panel, matching other cards' small info-box convention
panel_x, panel_y, panel_w, panel_h = 1000, 50, 230, 150
d.rectangle([panel_x, panel_y, panel_x + panel_w, panel_y + panel_h], outline=LINE, width=1)
d.text((panel_x + 14, panel_y + 12), "MCP TOOLS", font=f_label, fill=CYAN)
for i, label in enumerate(["speak_avatar", "list_voices", "play_vrma_animation", "set_display_scale"]):
    d.text((panel_x + 14, panel_y + 40 + i * 24), f"- {label}", font=f_mono, fill=DIM)

# bottom-left small caption block, matching "PIPELINE OVERVIEW" style boxes
cap_x, cap_y, cap_w, cap_h = 50, 610, 300, 70
d.rectangle([cap_x, cap_y, cap_x + cap_w, cap_y + cap_h], outline=LINE, width=1)
d.text((cap_x + 14, cap_y + 12), "PLACEHOLDER ILLUSTRATION", font=f_label, fill=WARM)
d.text((cap_x + 14, cap_y + 34), "replace when a real render is ready", font=f_mono, fill=DIM)

out_path = "/Users/kazus/Work/myprofile/profile-site/assets/work-tts-avatar.webp"
img.save(out_path, "WEBP", quality=90)
print("wrote", out_path)
