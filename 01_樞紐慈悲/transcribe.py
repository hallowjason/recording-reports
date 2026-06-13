import json
import mlx_whisper

AUDIO = "shum_cibei.wav"
MODEL = "model_q4"

# 繁體 + 佛學語境提示，降低錯字、引導用詞
PROMPT = "以下是一場關於樞紐、慈悲、修行、壇主、道場的中文開示與討論。請使用繁體中文。"

result = mlx_whisper.transcribe(
    AUDIO,
    path_or_hf_repo=MODEL,
    language="zh",
    initial_prompt=PROMPT,
    word_timestamps=False,
    verbose=False,
)

# 全文
with open("transcript_raw.txt", "w", encoding="utf-8") as f:
    f.write(result["text"].strip())

# 帶時間戳記的分段
segs = []
for s in result["segments"]:
    segs.append({"start": round(s["start"], 2), "end": round(s["end"], 2), "text": s["text"].strip()})
with open("transcript_segments.json", "w", encoding="utf-8") as f:
    json.dump(segs, f, ensure_ascii=False, indent=2)

# 帶時間的可讀版
def ts(sec):
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

with open("transcript_timed.txt", "w", encoding="utf-8") as f:
    for s in segs:
        f.write(f"[{ts(s['start'])}] {s['text']}\n")

print("DONE", len(segs), "segments")
