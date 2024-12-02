# OmniAI

## 项目概述

本项目构建了一个基于大模型技术（如 Ollama 模型框架）和人工通用智能（AGI）技术的智能助手，该智能助手具备长短期记忆、工具调用、计划、执行等多项能力，能够帮助一线工作人员提升工作效率，并具备行业专家的相关能力。

通过结合先进的自然语言处理技术，智能助手能够在特定领域中提供精确的操作指导、业务决策支持和问题解决方案。它的设计使得它能够灵活适应各种行业应用场景，从而提高工作效率并降低操作复杂度。

> **注意**：当前该产品仍处于测试阶段，提供的知识库内容仅为测试用途，实际投入使用时，用户需要根据自身需求添加行业相关知识。

## 核心功能

- **行业专家能力**：智能助手具备特定行业的专业知识，能够回答行业内的相关问题。
- **长短期记忆**：智能助手能够记住用户的短期输入（例如某次提问内容）和长期信息（例如用户常用的操作习惯或需求），提高后续交互的效率和智能化程度。
- **工具调用**：助手可以调用外部工具进行联网查询、文档搜索等操作，扩大其回答范围和准确性。
- **计划与执行**：具备基本的任务管理和执行能力，帮助用户规划工作任务并有效执行。
- **自动化决策**：利用大模型技术，助手不仅能提供信息，还能够根据用户的需求自动化生成解决方案，并执行相关任务。
- **文档与知识库管理**：智能助手能够处理并从本地文档（如 `.docx` 和 `.pdf` 文件）中提取信息，自动更新本地知识库，持续增强其行业知识。

## 系统架构

本系统基于大模型技术和AGI技术，采用模块化架构设计。各模块包括：

- **Interaction模块**：负责与用户的交互，处理用户输入，并将其与本地知识库、文档内容进行匹配。无法找到答案时，会调用外部大模型进行联网查询。
- **Memory模块**：负责存储短期和长期记忆。短期记忆存储最近的用户输入，长期记忆存储更持久的信息，提升系统的智能化程度。
- **Knowledge模块**：用于管理和查询本地知识库文件，支持动态加载、更新和存储知识。
- **WebSearch模块**：支持联网查询，集成外部大模型（如 qwen2），可以获取外部数据进行问题回答。
- **工具调用模块**：可以通过调用外部API和工具实现更多功能，如气象查询、供应链数据分析等。

## 安装与配置

### 环境要求

- **操作系统**：支持 Windows、macOS、Linux。
- **Python版本**：3.6 及以上。
- **依赖库**：
  ```bash
  pip install ollama~=0.4.0
  pip install docx~=0.2.4
  pip install python-docx~=1.1.2
  pip install pdfplumber~=0.11
