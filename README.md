# cx-1000-wiki

TOA **CX-1000** 系統的客戶技術 wiki 原始檔（MkDocs Material）。

🌐 線上站台：<https://tet-tw.github.io/cx-1000-wiki/>

## 內容
系統規格、設定 SOP、整合方案（攝影機事件、外部緊急系統、校園廣播橋接、WebAPI）、常見問題。
所有內容皆為本公司自行整理／改寫，**不含 TOA 手冊逐字內容**。

## 維護方式
1. 編輯 `docs/` 內的 markdown（或直接在 GitHub 網頁上改）。
2. `git push` 到 `main`。
3. GitHub Actions 會自動用 MkDocs 重建並部署到 GitHub Pages。

### 本機預覽（選用）
```bash
pip install -r requirements.txt
mkdocs serve      # http://127.0.0.1:8000
```

## 結構
```
docs/
├── index.md                 首頁
├── system/                  系統介紹（架構・設備・優先權）
├── guides/                  設定指南（初始化・緊急廣播）
├── integrations/            整合方案
└── faq.md                   常見問題
mkdocs.yml                   站台設定與導覽
.github/workflows/deploy.yml 自動部署
```

> 內部完整資料（含原廠手冊轉檔）另見私有 repo `cx-1000-base`。
