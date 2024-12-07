# 🌟 <span style="color: #3498db;">OmniAI</span>  

<div align="center">  

简体中文 / [繁体中文](README_TC.md) / [English](README.md) / [Deutsch](README_DE.md) / [日本語](README_JP.md)

</div>  

---

## 🌐 <span style="color: #2ecc71;">项目概述</span>  

本项目基于大型模型技术（如 ❤️ <span style="color: #e74c3c;">Ollama模型框架</span>）和通用人工智能（AGI）技术，构建了一个智能助手。  

该智能助手具备多种能力，包括：  
- 🧠 **短期和长期记忆**  
- 🔧 **工具调用**  
- 📋 **规划与执行**  

旨在提升前线工作人员的工作效率，并赋予他们行业专家的相关能力。通过整合先进自然语言处理技术，智能助手能够提供精确的操作指导、商业决策支持以及针对特定领域的解决方案。其设计适用于多种行业应用场景，从而简化工作流程，降低运营复杂性。  

> 💡 <span style="color: #f1c40f;">**注意**</span>：本产品目前处于测试阶段，提供的知识库内容仅供测试使用。在实际环境中部署产品时，用户需要根据需要融入行业特定的知识。  

---

## 🚀 <span style="color: #9b59b6;">核心功能</span>  

- 🏭 **<span style="color: #1abc9c;">行业专家能力</span>**  
  智能助手具备特定行业的专业知识，能够解答行业相关问题。  

- 📚 **<span style="color: #3498db;">短期和长期记忆</span>**  
  能够回忆用户的短期输入（如特定问题内容）和长期信息（如用户的操作习惯或需求），提高互动效率和智能化水平。  

- ⚙️ **<span style="color: #e67e22;">工具调用</span>**  
  支持调用外部工具（如网络搜索和文件检索），扩大回答范围并提升准确性。  

- 🗓️ **<span style="color: #95a5a6;">规划与执行</span>**  
  提供任务管理与执行功能，帮助用户高效规划与完成工作任务。  

- 🤖 **<span style="color: #f39c12;">自动化决策</span>**  
  利用大型模型技术，根据用户需求生成解决方案并自动执行相关任务。  

- 📂 **<span style="color: #2c3e50;">文件与知识库管理</span>**  
  支持本地文件（如 `.docx` 和 `.pdf`）的信息提取与处理，自动更新知识库并持续丰富行业知识。  

---

## 🛠️ <span style="color: #8e44ad;">系统架构</span>  

系统基于大型模型技术和AGI，采用模块化架构，具体模块如下：  

- 💬 **<span style="color: #16a085;">交互模块</span>**  
  处理用户交互、解析输入，并与本地知识库与文件内容匹配。当本地无回应时，启动网络搜索并利用外部大型模型补充。  

- 🧠 **<span style="color: #34495e;">记忆模块</span>**  
  管理短期与长期记忆，短期记忆存储最近用户输入，长期记忆保留更持久的信息以提升智能交互。  

- 📖 **<span style="color: #e74c3c;">知识模块</span>**  
  动态加载、更新、存储与查询本地知识库文件。  

- 🌐 **<span style="color: #f1c40f;">网络搜索模块</span>**  
  提供网络搜索功能，整合外部大型模型（如 qwen2），检索外部数据以回答问题。  

- 🔗 **<span style="color: #d35400;">工具调用模块</span>**  
  调用外部API与工具，支持功能扩展，如天气报告与供应链数据分析。  

---

## ⚙️ <span style="color: #2c3e50;">安装与配置</span>  

### 🌍 <span style="color: #95a5a6;">环境要求</span>  

- 💻 **<span style="color: #1abc9c;">操作系统</span>**：兼容 Windows、macOS、Linux  
- 🐍 **<span style="color: #3498db;">Python版本</span>**：3.6或更高  
- 📦 **<span style="color: #e67e22;">依赖库</span>**：  

```bash
pip install ollama~=0.4.0
pip install docx~=0.2.4
pip install python-docx~=1.1.2
pip install pdfplumber~=0.11.2
```  

✨ 现在一切就绪！开启您的智能探索之旅吧！ 🎉  