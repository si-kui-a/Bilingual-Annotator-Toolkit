# examples/

實際由本 repo 兩個 skill 產出格式所生成的範例 HTML（手動依 SKILL.md 規格產出，非 skill 自動執行結果，但完全依規格逐項對照）。

## 內容

| 檔案 | Skill | 內容 |
|---|---|---|
| `bilingual-doc-annotator/einstein-1905-emc2-excerpt.html` | bilingual-doc-annotator | DOC_TYPE=academic，DE → 繁體中文，節錄 Einstein 1905 論文開篇句與結論句各一段 |
| `study-visual-generator/einstein-1905-emc2-quiz.html` | study-visual-generator (TYPE_A) | 對應上述兩段的理解題，折疊答案卡，以 `對應Qn` 雙向連結 |

## 來源與授權（使用前必讀）

- 原文：Albert Einstein, *Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?*, Annalen der Physik 18 (1905), 639–641。
- **著作權狀態**：Einstein 1955 年逝世。EU 著作權年限為 death+70（計至該年年底），即 **2025/12/31 到期**。以生成時間點（2026）判斷，德文原文文字已進入公有領域，可自由重製。
- **未採用之素材**：未直接下載／重製 [Uni Augsburg Annalen der Physik Historic Papers](https://myweb.rz.uni-augsburg.de/~eckern/adp/history/Einstein-in-AdP.htm) 站上的期刊掃描 PDF ——掃描檔本身的排版／影像可能存在獨立於原文之外的權利歸屬，該站也未標示明確的重製授權條款。
- **實際採用之素材**：僅節錄兩句經多方獨立來源交叉驗證、逐字一致的公有領域原文（開篇句、結論句），非全文轉載。完整全文請自行取用上述 Uni Augsburg 連結，或 [de.Wikisource / Internet Archive](https://de.wikisource.org/wiki/Albert_Einstein) 掃描檔。
- **翻譯／問答內容**：中文譯文、批注文字、理解題與答案，均為本次示範原創撰寫，非引用任何第三方譯本或教材。

## GitHub Pages 靜態預覽（非阻斷，可延後）

之後要做的話，最省事路徑：`/docs` 資料夾直接放這些 HTML，repo Settings → Pages → Source 選 `main /docs`，不需要 build step。
