# CX-1000 技術 Wiki

TOA **CX-1000** IP 對講／廣播系統的技術參考站 —— 把系統規格、設定 SOP 與各種**可行的整合方案**整理成好理解、可持續更新的版本。

!!! note "這個站給誰看"
    系統整合商、工程人員與客戶。內容以「**看得懂、做得出來**」為目標，涵蓋基本規格到實際整合做法。

!!! tip "🤖 想用 AI 問這份 wiki？"
    我們把**整份 wiki 整理成一個 AI 好讀的檔案**。把下面的連結**貼進你的 ChatGPT / Claude 等 AI 對話框**（或複製其內容貼上），就能直接問，例如：「CX-1000 的緊急廣播優先權怎麼設？」「AF1062 的控制輸出是乾接點嗎？」

    [:material-file-document-outline: 開啟 llms-full.txt（整份 wiki 純文字）](https://tet-tw.github.io/cx-1000-wiki/llms-full.txt){ target=_blank rel=noopener }

    <button class="md-button md-button--primary" onclick="navigator.clipboard.writeText('https://tet-tw.github.io/cx-1000-wiki/llms-full.txt').then(()=>{this.textContent='已複製連結 ✓'})">複製連結給 AI</button>

    小提醒：若你的 AI 無法讀取網址，請開啟上面連結、全選內容複製，再貼進對話框即可（整份約 3 萬字，主流聊天室都貼得下）。

<div class="grid cards" markdown>

-   :material-sitemap:{ .lg .middle } &nbsp;__系統介紹__

    ---

    CX-1000 是什麼、有哪些設備、廣播優先權怎麼運作。

    [:octicons-arrow-right-24: 系統架構](system/overview.md) ·
    [設備與規格](system/devices.md) ·
    [廣播與優先權](system/priority.md)

-   :material-cog-play:{ .lg .middle } &nbsp;__設定指南__

    ---

    從系統初始化到緊急廣播的實際設定步驟。

    [:octicons-arrow-right-24: 快速上手](guides/quickstart.md) ·
    [緊急廣播設定](guides/emergency.md)

-   :material-connection:{ .lg .middle } &nbsp;__整合方案__

    ---

    攝影機事件、外部緊急系統、校園廣播、WebAPI 的整合做法。

    [:octicons-arrow-right-24: 整合總覽](integrations/index.md)

-   :material-help-circle:{ .lg .middle } &nbsp;__常見問題__

    ---

    卡在緊急模式、音檔註冊失敗、極性、優先權…疑難排解。

    [:octicons-arrow-right-24: 常見問題](faq.md)

</div>

---

!!! warning "重要聲明"
    - 本站為 **tet-tw 整理之技術資料**，非 TOA 官方文件；實際規格與操作以 TOA 原廠手冊與韌體為準。
    - 文中所述之緊急／整合應用**非 EN54、非消防認證**，**不得取代法規要求的消防偵測與疏散系統**。
