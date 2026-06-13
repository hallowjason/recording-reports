#!/usr/bin/env python3
"""以 Gemini 2.5 Flash Image (Nano Banana) 生圖。
用法: python3 gen_img.py "<prompt>" <out_path.png> [aspect]
aspect: 16:9 (預設) / 4:3 / 1:1 / 3:4 / 9:16
"""
import sys, os, base64, json, urllib.request

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

prompt = sys.argv[1]
out = sys.argv[2]
aspect = sys.argv[3] if len(sys.argv) > 3 else "16:9"

body = {
    "contents": [{"parts": [{"text": prompt}]}],
    "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": aspect}},
}

req = urllib.request.Request(
    URL, data=json.dumps(body).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)
try:
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.load(r)
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode()[:800]); sys.exit(1)

saved = False
for cand in data.get("candidates", []):
    for part in cand.get("content", {}).get("parts", []):
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("data"):
            with open(out, "wb") as f:
                f.write(base64.b64decode(inline["data"]))
            print("SAVED", out, os.path.getsize(out), "bytes")
            saved = True
            break
    if saved:
        break
if not saved:
    print("NO IMAGE. Response:", json.dumps(data)[:800]); sys.exit(2)
