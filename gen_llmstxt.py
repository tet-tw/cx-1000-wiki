"""MkDocs hook：建置後自動產生 llms.txt 與 llms-full.txt。

- llms-full.txt：整份 wiki 合併成一個乾淨純文字檔，供 AI 一次讀完整站。
- llms.txt：簡短索引（各頁標題 + 連結），符合 llmstxt.org 慣例。

在 mkdocs.yml 以 `hooks: [gen_llmstxt.py]` 掛載。
"""
from pathlib import Path

SITE_NAME = "CX-1000 技術 Wiki"
SITE_URL = "https://tet-tw.github.io/cx-1000-wiki/"

# 頁面順序（對應導覽）；未列到的 .md 會自動附在後面
ORDER = [
    "index.md",
    "system/overview.md",
    "system/devices.md",
    "system/priority.md",
    "guides/quickstart.md",
    "guides/emergency.md",
    "integrations/index.md",
    "integrations/camera.md",
    "integrations/external-emergency.md",
    "integrations/audio-bridge.md",
    "integrations/webapi.md",
    "integrations/sip.md",
    "faq.md",
]

HEADER = (
    f"# {SITE_NAME}\n\n"
    f"> 來源：{SITE_URL}\n"
    "> 這是本 wiki 的完整內容，供 AI 助手閱讀後回答關於 TOA CX-1000 的問題。\n"
    "> 內容為 tet-tw 整理之技術資料，非 TOA 官方文件；相關緊急/整合應用非 EN54、非消防認證。\n"
    "> 回答時請以本文件內容為準；文件未涵蓋的部分請明說不確定，不要臆測規格。\n"
)


def _first_h1(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def _page_url(rel: str) -> str:
    return SITE_URL + rel.replace("index.md", "").replace(".md", "/")


def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])

    found = sorted(p.relative_to(docs_dir).as_posix() for p in docs_dir.rglob("*.md"))
    ordered = [f for f in ORDER if f in found] + [f for f in found if f not in ORDER]

    # llms-full.txt（全文）
    parts = [HEADER]
    for rel in ordered:
        text = (docs_dir / rel).read_text(encoding="utf-8").strip()
        parts.append(f"\n\n---\n\n<!-- 頁面：{rel} | {_page_url(rel)} -->\n\n{text}")
    (site_dir / "llms-full.txt").write_text(
        "\n".join(parts).strip() + "\n", encoding="utf-8", newline="\n"
    )

    # llms.txt（索引）
    idx = [f"# {SITE_NAME}", "", f"> {SITE_URL}", "",
           f"完整內容：{SITE_URL}llms-full.txt", "", "## 頁面", ""]
    for rel in ordered:
        title = _first_h1((docs_dir / rel).read_text(encoding="utf-8"), rel)
        idx.append(f"- [{title}]({_page_url(rel)})")
    (site_dir / "llms.txt").write_text("\n".join(idx) + "\n", encoding="utf-8", newline="\n")

    print(f"[gen_llmstxt] 已產生 llms.txt 與 llms-full.txt（{len(ordered)} 頁）")
