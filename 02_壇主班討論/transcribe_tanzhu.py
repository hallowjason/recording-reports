import json
import mlx_whisper

AUDIO = "02_壇主班討論/tanzhu.wav"
MODEL = "model_q4"

# 繁體 + 道場語境提示，降低錯字、引導用詞
PROMPT = "以下是一場關於壇主、道場、修行、開荒、辦道、點傳師的中文討論與開示。請使用繁體中文。"

result = mlx_whisper.transcribe(
    AUDIO,
    path_or_hf_repo=MODEL,
    language="zh",
    initial_prompt=PROMPT,
    word_timestamps=False,
    verbose=False,
)

with open("02_壇主班討論/transcript_raw.txt", "w", encoding="utf-8") as f:
    f.write(result["text"].strip())

segs = []
for s in result["segments"]:
    segs.append({"start": round(s["start"], 2), "end": round(s["end"], 2), "text": s["text"].strip()})
with open("02_壇主班討論/transcript_segments.json", "w", encoding="utf-8") as f:
    json.dump(segs, f, ensure_ascii=False, indent=2)

def ts(sec):
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

with open("02_壇主班討論/transcript_timed.txt", "w", encoding="utf-8") as f:
    for s in segs:
        f.write(f"[{ts(s['start'])}] {s['text']}\n")

print("DONE", len(segs), "segments")
