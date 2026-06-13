#!/usr/bin/env python3
"""批次生成壇主班報告的所有關鍵視覺（溫暖人文紀實攝影風，與 hero 一致）。"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "assets", "img")
GEN = os.path.join(HERE, "gen_img.py")

STYLE = ("warm candid documentary photograph, soft golden afternoon light, "
         "shallow depth of field, gentle film grain, warm amber honey and cream "
         "color palette, organic human and tender, faces soft or turned away, "
         "no text, no words, no typography, no logos")

JOBS = [
    # (filename, aspect, content + composition)
    ("pivot.png", "16:9",
     "an open wooden doorway in a sunlit room, warm golden light pouring through the threshold, "
     "a welcoming open space inviting someone in, gentle and hopeful, a sense of being welcomed rather than summoned, "
     "the doorway and light on the right two-thirds, left third soft warm empty light for text overlay"),
    ("audience.png", "16:9",
     "three young people of different ages standing softly side by side near a sunlit window, "
     "a teenager, an older youth, and a young adult, seen in gentle backlight as soft silhouettes, warm and quiet, "
     "evenly spaced across the frame with calm warm background"),
    ("ideas.png", "16:9",
     "close view of several hands of young people gathered around a wooden table writing on paper and arranging "
     "colorful sticky notes, a lively warm collaborative brainstorming moment, afternoon sun across the table, "
     "hands and papers fill the frame, cozy and creative"),
    ("messages.png", "3:4",
     "a single young person sitting quietly by a large sunlit window, peaceful and contemplative, "
     "soft warm light on their shoulder and hair, seen from behind or the side, a moment of calm and recharge, "
     "lots of gentle warm light, serene"),
    ("generations.png", "16:9",
     "a tender close-up of an elderly weathered hand gently holding a young person's hand, "
     "warm soft light, deeply emotional and intimate, conveying connection across generations, "
     "the joined hands centered, warm blurred background"),
    ("recharge.png", "3:4",
     "a person resting peacefully in warm afternoon light with eyes closed, a cup of tea nearby on a wooden surface, "
     "calm restorative and nourished, soft golden glow, a moment of being replenished, serene and gentle"),
    ("embrace.png", "16:9",
     "two people sharing a warm heartfelt embrace in soft golden light, reconciliation and understanding, "
     "seen at a gentle angle so faces are soft, deeply moving and tender, warm glowing background, "
     "the embrace slightly right of center, left area soft and warm for text"),
    ("dawn.png", "16:9",
     "soft dawn light streaming through a window over a quiet peaceful room with simple wooden furniture, "
     "early morning hope and new beginnings, calm and warm, empty and serene, gentle golden glow, "
     "wide tranquil composition"),
]

failed = []
for fn, aspect, content in JOBS:
    out = os.path.join(OUT, fn)
    prompt = f"{content}. {STYLE}."
    print(f"\n=== {fn} ({aspect}) ===", flush=True)
    r = subprocess.run([sys.executable, GEN, prompt, out, aspect])
    if r.returncode != 0:
        failed.append(fn)

print("\nFAILED:", failed if failed else "none")
