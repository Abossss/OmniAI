# <span style="color: #3498db;">OmniAI</span>

<div align="center">

[简体中文](README_CN.md) / 繁體中文 / [English](README.md)

</div>


## <span style="color: #2ecc71;">項目概述</span>
本項目基於大型模型技術（如<span style="color: #e74c3c;">Ollama模型框架</span>）和通用人工智能（AGI）技術，構建了一個智能助手。該智能助手具備多種能力，包括短期和長期記憶、工具調用、規劃、執行等。旨在提升前線工作人員的工作效率，並賦予他們行業專家的相關能力。

通過整合先進自然語言處理技術，智能助手能夠提供精確的操作指導、商業決策支持和針對特定領域的解決方案。其設計適應於多種行業應用場景，從而簡化工作流程，降低運營複雜性。

> <span style="color: #f1c40f;">**注意**</span>：本產品目前處於測試階段，提供的知識庫內容僅供測試使用。在實際環境中部署產品時，用戶需要根據需要融入行業特定的知識。

## <span style="color: #9b59b6;">核心功能</span>
- **<span style="color: #1abc9c;">行業專家能力</span>**：智能助手具備特定行業的專業知識，能夠解答行業相關問題。
- **<span style="color: #3498db;">短期和長期記憶</span>**：助手能夠回憶用戶的短期輸入（例如特定問題的內容）和長期信息（例如用戶的常見操作習慣或需求），提高後續互動的效率和智慧性。
- **<span style="color: #e67e22;">工具調用</span>**：助手可以調用外部工具進行操作，如網絡搜索和文件檢索，擴大回答的範圍和準確性。
- **<span style="color: #95a5a6;">規劃和執行</span>**：提供基本的任務管理和執行能力，幫助用戶有效規劃執行工作任務。
- **<span style="color: #f39c12;">自動化決策</span>**：利用大型模型技術，助手不僅提供信息，還可以根據用戶的需求自動生成解決方案並執行相關任務。
- **<span style="color: #2c3e50;">文件和知識庫管理</span>**：智能助手能夠處理和提取本地文件（例如 `.docx` 和 `.pdf` 文件）的信息，自動更新本地知識庫，並持續豐富其行業知識。

## <span style="color: #8e44ad;">系統架構</span>
系統基於大型模型技術和AGI，採用模塊化架構。模塊如下：
- **<span style="color: #16a085;">交互模塊</span>**：處理用戶交互，處理用戶輸入，並與本地知識庫和文件內容進行匹配。當本地無法提供迴應時，它會啓動網絡搜索，使用外部大型模型。
- **<span style="color: #34495e;">記憶模塊</span>**：管理短期和長期記憶。短期記憶捕捉最後的用戶輸入，而長期記憶保留更持久的資訊，增強系統的智慧。
- **<span style="color: #e74c3c;">知識模塊</span>**：管理和查詢本地知識庫文件，支持動態加載、更新和存儲知識。
- **<span style="color: #f1c40f;">網絡搜索模塊</span>**：提供網絡搜索功能，整合外部大型模型（如qwen2），並檢索外部數據以回答問題。
- **<span style="color: #d35400;">工具調用模塊</span>**：通過調用外部API和工具擴展功能，例如天氣報告和供應鏈數據分析。

## <span style="color: #2c3e50;">安裝與配置</span>
### <span style="color: #95a5a6;">環境要求</span>
- **<span style="color: #1abc9c;">操作系統</span>**：兼容Windows、macOS、Linux。
- **<span style="color: #3498db;">Python版本</span>**：3.6或更高。
- **<span style="color: #e67e22;">依賴庫</span>**：
```bash
pip install ollama~=0.4.0
pip install docx~=0.2.4
pip install python-docx~=1.1.2
pip install pdfplumber~=0.11