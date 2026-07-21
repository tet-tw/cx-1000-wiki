# SIP 電話整合（功能盤點）

CX-1000 內建 SIP 伺服器（由 SM1000 擔任），可讓 **SIP 話機** 與 **外部電話系統（VoIP adapter / IP-PBX）** 和 CX 站台互打。本頁盤點 SIP 的能力、設定、需求與限制。

!!! note "✅ 原廠標準功能"
    SIP 為 CX-1000 原廠內建功能，屬 TOA 原廠手冊範圍，不需自研軟體。

---

## 定位：SM1000 自己就是 SIP 伺服器
- **CX-SM1000 擔任 SIP 註冊/認證伺服器**；全系統通話以 SIP 控制，但**語音串流走 P2P Direct Media**（站台間直接傳、不經 SM1000）。
- **每台 CX 裝置都有 SIP 身分**；CX 站台與 SIP 話機的 **SIP ID＝站號、不可更改**（只有外部電話介面的 SIP ID 可逐線改）。
- **沒有「SIP server 位址」欄位**要填 —— server 內建在 SM1000。

## 涉及的設備 + 容量
| 對象 | 與 SIP 的關係 | 上限 |
|---|---|---|
| CX 站台（OP／CL／RM／AF／PA／CC） | SIP ID＝站號，內部通話以 SIP 控制 | 系統總量 3000 |
| **一般 SIP 話機** | 註冊為「SIP Phone」與 CX 互打 | **100 台** |
| **外部電話介面**（VoIP adapter / IP-PBX） | 以 SIP 接外線，SIP ID 可逐線改 | **8 條**（兩種介面**同系統二選一、不可混用**） |
| **IP-A1 系列** | 可註冊為 SIP Phone → 撥號即對它做**個別麥克風廣播** | — |

---

## 呼叫能力（誰能打誰）

### SIP 話機 ↔ CX 站台
- **個別呼叫**、**群呼**、應答（**純語音**）。

### SIP 話機用撥號碼控制
- **接點橋接（Contact bridge）**：`*31`／`*32` ＋ 控制輸出群組 → 開／關控制輸出
- **門禁遠端**：通話中 `**5X0`／`**5X1`（X＝1~5）
- **外撥外線**：撥 special number 接通 → 聽外線撥號音 → 撥號

### 外線 → CX
- **DIL（直入線）**：外撥 → 響到預設站台／群組
- **DID（直撥指定站）**：外撥 → 二次撥號音 → 直撥站號（逾 5 秒斷、逾 30 秒轉 DIL）
- 掛斷碼 `00#` 或忙音偵測掛斷

### CX 站台側
- 對外撥打（撥號鍵／Direct 鍵／OP1700 聯絡簿）、**One-touch dial**、**Remote dial**（控制輸入觸發自動撥號，可撥站號／群呼／外線）。

---

## 設定在哪（4 個地方）
| 畫面 | 設什麼 |
|---|---|
| `Network (Device) → SIP` | 每台／每線的 **SIP ID／Password／SIP port**（預設 5060）；要勾 **Customize SIP settings** 才顯示 |
| `Intercom → Station number` | 站號位數（2–8）、**Automatic allocation**（自動配「站號＝SIP ID＝密碼」，由 1 起連號） |
| `Network (System) → Broadcast/Call` | 系統 **SIP port**（1025–65535，預設 5060） |
| `Intercom → External telephone system` | 線路數 1–8、介面（IP-PBX／VoIP adapter）、最長通話、**special number**、DID／DIL 開關、DIL 接收站、DTMF send delay |

---

## SIP 話機相容需求（要能跟 CX 互通）
!!! tip "採購 SIP 話機前必看"
    - ✅ **必備**：音訊 **G.722 ＋ G.711**、支援 **Direct Media**、**DTMF 用 SIP INFO**。
    - ⚙️ **關閉／注意**：**Early Media 要關**；與 CX **無視訊（純語音）**；**勿用會自動應答的話機**（尤其別放進群組）。

外部電話系統（VoIP adapter／IP-PBX）需求：DTMF 僅 SIP INFO、走 UDP、支援 Direct Media、**忙音偵測送 BYE**、每線不重複 SIP ID。

---

## ⚠ 限制與眉角（重點）
- ❌ **無視訊** —— 與 SIP 話機／外部分機只能語音，即使 PBX 有視訊也不行。
- ❌ **不支援 PTT 單向對講**。
- ❌ **不能從 SIP 話機／外線手動轉接**到 CX 站台。
- ❌ **DTMF 只吃 SIP INFO**（不支援 in-band／RFC2833）→ 外部設備要能轉成 SIP INFO。
- ❌ **VoIP adapter 與 IP-PBX 同系統二選一**，不可混用。
- ⚠ Jitter buffer 設「Low latency」時，**SIP 話機通話可能不穩／有雜訊**。
- ⚠ **跨路由器／異地** multicast（廣播）可能不通；但 **SIP 通話走 P2P unicast、較好過 WAN**（多廠對講走 SIP 比廣播友善）。

---

## 網路 / 埠
- **SIP：埠 5060 ／ 走 UDP**。
- 其他預設埠：Call audio `20000`、Call video `40000`、Broadcast audio `17000`、Control `15001`、IP camera `60000`。

---

## 重點整理
- **SM1000 內建 SIP 伺服器**；最多 **100 台 SIP 話機** ＋ **8 條外線**（VoIP adapter 或 IP-PBX 二選一）與 CX 站台互打。
- 支援**群呼、DID／DIL、撥號碼控制接點／門禁**。
- **只有語音（無視訊）**、**DTMF 限 SIP INFO**；SIP 話機需 **G.722／G.711 ＋ Direct Media ＋ SIP INFO**。
- 異地多廠：**對講走 SIP（unicast）較可行**，廣播（multicast）需另做網路工程。
