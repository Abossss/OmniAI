# <span style="color: #3498db;">OmniAI</span>

<div align="center">

简体中文 / [繁体中文](README_TC.md) / [English](README.md)

</div>


## <span style="color: #2ecc71;">项目概述</span>
本项目基于大型模型技术（如<span style="color: #e74c3c;">Ollama模型框架</span>）和通用人工智能（AGI）技术，构建了一个智能助手。该智能助手具备多种能力，包括短期和长期记忆、工具调用、规划、执行等。旨在提升前线工作人员的工作效率，并赋予他们行业专家的相关能力。

通过整合先进自然语言处理技术，智能助手能够提供精确的操作指导、商业决策支持和针对特定领域的解决方案。其设计适应于多种行业应用场景，从而简化工作流程，降低运营复杂性。

> <span style="color: #f1c40f;">**注意**</span>：本产品目前处于测试阶段，提供的知识库内容仅供测试使用。在实际环境中部署产品时，用户需要根据需要融入行业特定的知识。

## <span style="color: #9b59b6;">核心功能</span>
- **<span style="color: #1abc9c;">行业专家能力</span>**：智能助手具备特定行业的专业知识，能够解答行业相关问题。
- **<span style="color: #3498db;">短期和长期记忆</span>**：助手能够回忆用户的短期输入（例如特定问题的内容）和长期信息（例如用户的常见操作习惯或需求），提高后续互动的效率和智慧性。
- **<span style="color: #e67e22;">工具调用</span>**：助手可以调用外部工具进行操作，如网络搜索和文件检索，扩大回答的范围和准确性。
- **<span style="color: #95a5a6;">规划和执行</span>**：提供基本的任务管理和执行能力，帮助用户有效规划执行工作任务。
- **<span style="color: #f39c12;">自动化决策</span>**：利用大型模型技术，助手不仅提供信息，还可以根据用户的需求自动生成解决方案并执行相关任务。
- **<span style="color: #2c3e50;">文件和知识库管理</span>**：智能助手能够处理和提取本地文件（例如 `.docx` 和 `.pdf` 文件）的信息，自动更新本地知识库，并持续丰富其行业知识。

## <span style="color: #8e44ad;">系统架构</span>
系统基于大型模型技术和AGI，采用模块化架构。模块如下：
- **<span style="color: #16a085;">交互模块</span>**：处理用户交互，处理用户输入，并与本地知识库和文件内容进行匹配。当本地无法提供回应时，它会启动网络搜索，使用外部大型模型。
- **<span style="color: #34495e;">记忆模块</span>**：管理短期和长期记忆。短期记忆捕捉最后的用户输入，而长期记忆保留更持久的资讯，增强系统的智慧。
- **<span style="color: #e74c3c;">知识模块</span>**：管理和查询本地知识库文件，支持动态加载、更新和存储知识。
- **<span style="color: #f1c40f;">网络搜索模块</span>**：提供网络搜索功能，整合外部大型模型（如qwen2），并检索外部数据以回答问题。
- **<span style="color: #d35400;">工具调用模块</span>**：通过调用外部API和工具扩展功能，例如天气报告和供应链数据分析。

## <span style="color: #2c3e50;">安装与配置</span>
### <span style="color: #95a5a6;">环境要求</span>
- **<span style="color: #1abc9c;">操作系统</span>**：兼容Windows、macOS、Linux。
- **<span style="color: #3498db;">Python版本</span>**：3.6或更高。
- **<span style="color: #e67e22;">依赖库</span>**：
  ```bash
  pip install ollama~=0.4.0
  pip install docx~=0.2.4
  pip install python-docx~=1.1.2
  pip install pdfplumber~=0.11
