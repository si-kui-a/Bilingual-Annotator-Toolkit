---
name: study-visual-generator
description: 泛用學習視覺化HTML擴充包,獨立於bilingual-doc-annotator。涵蓋4種輸出類型:問題清單+折疊答案卡、知識地圖、單詞卡片、概念解析圖。語言不限,依使用者對話語言或指定TGT_LANG輸出。共用配色/字體系統(深海軍藍+米白/Lora+IBM Plex Sans)。
---
CONFIG: TGT_LANG(輸出語言,預設與使用者對話語言一致)

OUTPUT: 單一.html檔,create_file產出,不對話輸出。每種TYPE各自獨立檔案。

SHARED_STYLE: 導航深海軍藍|底色米白|正文Lora|介面IBM Plex Sans|批注卡左色邊+浅背景|Responsive移動端單欄|CJK/RTL語言需對應字體fallback與dir屬性

ROUTE(依需求選TYPE,可多選並行,若使用者僅給主題無細節→先問要哪個TYPE,禁止一次全生成):

===TYPE_A: 問題清單+折疊答案===
INPUT: 討論題清單(任意來源)
STRUCT: 每題獨立卡(題號+題目);答案預設折疊(<details><summary>);對應原文批注卡標註「對應Q{n}」建立雙向連結
RULE: 答案預設不展開;使用者要求「先看答案」則反轉

===TYPE_B: 知識地圖===
STRUCT: 中心節點→分支節點→葉節點,HTML+CSS或SVG畫節點連線圖
COLOR: 依節點層級深淺navy色階
RULE: 節點文字≤15字;超過20節點→分區塊呈現

===TYPE_C: 單詞卡片===
STRUCT: 正面=詞彙(SRC語言),背面=TGT_LANG釋義+例句+詞性
INTERACTION: CSS 3D flip優先無JS;需記錄進度才加JS state
FORMAT: 每卡獨立div,支援grid多卡排列

===TYPE_D: 概念解析===
STRUCT: 概念名→定義(1句,≤30字)→展開說明(3-5句)→相關概念標籤(可點擊錨點跳轉)
RULE: 展開說明避免重複定義句用詞;相關概念用同頁錨點連結

COMMON_RULE:
- 輸出語言=TGT_LANG,原文詞彙可保留SRC語言
- 禁止臆造來源資料未提及之細節
- 中文輸出時預設繁體,避免簡體用語(除非使用者明確要求簡體)
