# Session Context — 2026-06-13

## 資料夾結構（已重整）
- `01_樞紐慈悲/` — 樞紐慈悲專案（逐字稿、重點 md、報告、assets、音檔）
- `02_壇主班討論/` — 壇主班專案（**2026-06-13 本 session 新建完成**）
- 根目錄共用工具：`.venv` / `model_q4`（mlx-whisper）/ `node_modules`（puppeteer-core）

## 壇主班討論（02）— 已完成（本 session）
- 來源 `壇主班的討論.m4a`（102 分）→ mlx-whisper（model_q4）轉繁體逐字稿
- `壇主班_重點.md` — 10 章重點（青年壇主班課程設計腦力激盪會議）
- **`02_壇主班討論/index.html`** ⭐ 最終交付：**14 屏分頁 Web App**（用戶指定），點選／←→／space／Home-End 鍵切換、圓點導航、hash 路由、觸控滑動、進場 stagger 動畫
  - 各頁量身版面：封面(bleed) / 總綱(四關鍵字) / 核心定調(轉折+雙金句) / 三類學員(三卡) / 交通現實(圖文) / 七個點子(四欄8卡) / 給二代(圖+四卡) / 世代洞察(以前vs現在+大金句) / 賢德充電(圖文) / 新舊張力(四卡) / 擁抱破冰(bleed) / 結論待續 / 行動九格 / 結尾(bleed)
  - 暖蜜＋陶土「溫暖人文」配色；Noto Serif/Sans TC + Cormorant Garamond
  - **溯源功能**：頂列有「▶ 試聽此段（播對應錄音時間窗、Web Audio 放大 2.2x、自動停段尾）」+「☰ 逐字稿」hover tooltip（潤飾版＋虛線下原始 ASR 對照），切頁自動停止
- `02_壇主班討論/srcmap.js` — 14 頁 `{start,end,label,refined潤飾版,raw}`，由 transcript_segments.json 依關鍵詞錨點定位時間窗、潤飾逐字稿
- `02_壇主班討論/index_scroll.html` — 長捲動版備份（無溯源功能）
- `assets/img/` 9 張 **Gemini Nano Banana** 真實影像：hero/pivot/audience/ideas/messages/generations/recharge/embrace/dawn
- 生圖腳本 `gen_img.py`（單張）/ `gen_all.py`（批次）；轉錄 `transcribe_tanzhu.py`
- 驗證：puppeteer 全 14 頁截圖，0 console error，每頁一屏（頁7/9 各約 50px 內捲，可忽略）

## 已知踩過的坑（分頁版）
- bleed 頁的 `.cover{position:relative}` / `.closing{position:relative}` 會覆蓋 `.page{position:fixed}`（同特異度後者勝），導致頁高塌成內容高 → 移除多餘 position 即可
- `.page` 用 `position:fixed;inset:0` 最穩，不依賴 containing block
- 3:4 直式人像圖在分欄會撐高 → `.split .figure{max-height:58vh}` 上限

## 樞紐慈悲（01）— 已完成
- `20260613樞紐慈悲.m4a`（58 分）→ mlx-whisper large-v3-turbo 轉繁體逐字稿（transcript_*）
- `樞紐慈悲_重點.md` — 十大區塊重點整理
- **`01_樞紐慈悲/index.html`** ⭐ 最終交付：**11 分頁的單頁 Web App**（不是長捲動），暖米色+金線、Figma 結構底層、字級全 ≥20px
  - 各分頁不同版式：總覽(Hero) / 時機(左文右圖) / 三大主軸(三卡) / 兩條路線(對照表格) / 地理樞紐(地圖+網格) / 七年(垂直時間軸) / 公司化(理由+側圖) / 在地化(大引言+小圖) / 三層架構(階層圖) / 慈悲(蓮花置中+四卡) / 行動(勾選清單)
  - 互動：點分頁切換、← → 鍵切換、hash 路由、品牌回首頁
  - **溯源功能（新增）**：每分頁有「溯源列」→ ① 試聽此段（播放 m4a 對應時間窗、底部 now-playing bar、自動停在段尾）② hover「逐字稿」跳出該段 ASR 原文 tooltip
- `srcmap.js` — 每分頁對應的錄音時間窗 + 逐字稿（由 transcript_segments.json 依關鍵詞錨點產生），index.html 以 `<script src>` 載入
- `assets/img/` 9 張 codex imagegen 真實插圖：hero/timing/pillars/routes/map/ladder/vessel/localize/compassion

## 待辦 / 可選
- 逐字稿人名/地名為 ASR 推測（林島/銀南亞/邱東/黃蘭師等），有正確版可校正
- 清除根目錄與 01/ 內的 `_*.png` 截圖暫存（rm 權限被擋，需手動）

## 重要決策與限制
- **圖片必須真實 AI 生成、非 SVG**；驗收由用戶說了算（見全域記憶 prefers-real-images-over-svg）
- 生圖管道 = **codex CLI app 版** `/Applications/Codex.app/Contents/Resources/codex` 的內建 **imagegen**，走 ChatGPT 訂閱、不用 API key（API key 已達 billing limit）
- codex config 坑：用 app 版 codex；`~/.codex/config.toml` 的 `service_tier` 保持 `priority`
- 轉錄坑：HF 大檔限速 → `curl -C -` 直抓 weights 放本地，mlx 讀本地路徑
- 設計底層：figma DESIGN.md 結構 + 暖米色 + 金線意象

## 下次繼續
cd /Users/gooo/Desktop/.claude/projects/recording/01_樞紐慈悲
open index.html
