---
name: bilingual-doc-annotator
description: 泛用雙語批注HTML生成器。輸入任意來源語言文件+目標譯文語言,產出左欄(原文按維度高亮+意譯段落塊)+右欄(逐段批注)雙欄HTML。支援學術論文/文章/法律文件/文學/技術文件等文件類型,色彩維度依文件類型套預設或自訂。取代僅限中英學術論文的舊版。
---
CONFIG(每次任務先確認,若使用者未指定則詢問或用預設):
- SRC_LANG: 來源語言(預設偵測輸入文件語言)
- TGT_LANG: 譯文語言(預設: 與使用者對話語言一致)
- DOC_TYPE: academic|article|legal|literary|technical|custom(預設academic)
- TRANSLATION_MODE: 意譯(預設,讀感需像TGT_LANG母語寫作)|直譯(僅使用者明確要求時)

OUTPUT: 單一.html檔,create_file產出,不對話輸出。

STRUCTURE(4區塊,依序):
1. 頂部導航: 標題(文件名+context資訊)+顏色圖例(依DIM_PRESET)
2. 章節導航條: sticky,可跳轉各節
3. 主體雙欄:
   左欄(SRC_LANG原文+TGT_LANG譯文,逐段):
     ①原文,依DIM_PRESET高亮
     ②譯文,緊接原文段落下方,浅背景色塊(#f0ece2)+左側細豎線區隔,依TRANSLATION_MODE處理,不加顏色高亮
     原文與譯文間1px細分隔線
   右欄(逐段對應批注,語言=TGT_LANG):
     ①段落功能(依DOC_TYPE用對應功能標籤,見DOC_TYPE_FUNCTIONS)
     ②邏輯角色(該段在整體結構中的位置)
     ③技巧/漏洞或風險點(至少1項,依DOC_TYPE調整措辭)
4. 底部總覽: 全文邏輯骨架+核心主張/結論一句話版+最強處1條+最弱處(或最高風險)1條

DIM_PRESET(依DOC_TYPE切換,5色固定,語義可換):
| DOC_TYPE | 黃 | 紅 | 藍 | 綠 | 紫 |
|---|---|---|---|---|---|
| academic | 核心論點 | 關鍵術語 | 實證數據 | 讓步/反駁 | 方法論 |
| article | 核心主張 | 關鍵詞彙 | 引用/數據 | 對立觀點 | 寫作手法 |
| legal | 核心義務 | 法律定義 | 條款依據 | 例外/除外條款 | 適用程序 |
| literary | 主題意象 | 關鍵詞/意象詞 | 文本證據 | 反諷/對比 | 敘事手法 |
| technical | 核心結論 | 技術術語 | 實驗數據 | 限制/邊界條件 | 方法/流程 |
| custom | 使用者自訂5維度,任務開始前先問 |

DOC_TYPE_FUNCTIONS(右欄段落功能標籤依DOC_TYPE切換):
| DOC_TYPE | 功能標籤範例 |
|---|---|
| academic | 引出問題/提供證據/反駁異議/總結 |
| article | 開場鉤子/論述展開/案例佐證/收束 |
| legal | 定義/課予義務/設定例外/罰則 |
| literary | 場景鋪陳/意象建立/衝突推進/主題收束 |
| technical | 問題陳述/方法描述/結果呈現/限制討論 |

STYLE(固定,不隨語言/文件類型變動):
- 導航: 深海軍藍(navy) | 底色: 米白(paper-white)
- 字體: 正文Lora(serif) | 介面IBM Plex Sans;若SRC_LANG/TGT_LANG含CJK,正文字體加中文/日文/韓文對應serif fallback(如Noto Serif TC/JP/KR)
- 譯文塊: #f0ece2背景+左細豎線
- 批注卡: 左色邊+浅背景
- Responsive: 移動端強制單欄

RULE:
- TRANSLATION_MODE=意譯時,禁逐字直譯,讀感須為流暢TGT_LANG母語寫作;=直譯時保留原句結構
- 譯文區塊不套用五色高亮
- 批注須逐段對應,不得跳段/合併
- SRC_LANG/TGT_LANG非拉丁字母(阿拉伯文/希伯來文等RTL語言)→左欄原文區塊需設dir="rtl"
- DOC_TYPE=custom→執行前必須先向使用者確認5維度定義,不得自行假設

EXTENSION_HOOK: 使用者可疊加`study-visual-generator`skill產出延伸學習工具(問題清單/知識地圖/單詞卡/概念解析),兩skill獨立運作,不強制合併輸出。
