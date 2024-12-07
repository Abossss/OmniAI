# 🌟 <span style="color: #3498db;">OmniAI</span>  

<div align="center">
 
[简体中文](README_CN.md) / [繁体中文](README_TC.md) / English / [Deutsch](README_DE.md) / [日本語](README_JP.md)

</div>  

---

## 🌐 <span style="color: #2ecc71;">Project Overview</span>  

This project constructs an intelligent assistant leveraging large model technologies (such as the ❤️ <span style="color: #e74c3c;">Ollama model framework</span>) and Artificial General Intelligence (AGI) technologies.  

The intelligent assistant features multiple capabilities including:  
- 🧠 **Short-term and long-term memory**  
- 🔧 **Tool invocation**  
- 📋 **Planning and execution**  

It aims to enhance the work efficiency of front-line workers and equip them with the competencies of industry experts. By integrating advanced natural language processing technologies, the assistant provides precise operational guidance, business decision support, and tailored solutions. Its design facilitates adaptability to a variety of industry application scenarios, streamlining work processes and reducing operational complexity.  

> 💡 <span style="color: #f1c40f;">**Note**</span>: This product is currently in the testing phase. The knowledge base is for testing purposes only. When deploying in a live environment, users should incorporate industry-specific knowledge as needed.  

---

## 🚀 <span style="color: #9b59b6;">Core Functions</span>  

- 🏭 **<span style="color: #1abc9c;">Industry Expert Capability</span>**  
  Possesses professional knowledge in specific industries to address industry-related queries.  

- 📚 **<span style="color: #3498db;">Short-term and Long-term Memory</span>**  
  Recalls recent user inputs and retains long-term information like user habits, improving interaction efficiency.  

- ⚙️ **<span style="color: #e67e22;">Tool Invocation</span>**  
  Utilizes external tools for operations such as web searches and document retrieval, broadening response accuracy.  

- 🗓️ **<span style="color: #95a5a6;">Planning and Execution</span>**  
  Assists in task management and execution for effective work planning.  

- 🤖 **<span style="color: #f39c12;">Automated Decision-making</span>**  
  Autonomously generates solutions and executes tasks based on user needs.  

- 📂 **<span style="color: #2c3e50;">Document and Knowledge Base Management</span>**  
  Processes documents (e.g., `.docx` and `.pdf`), updates the knowledge base, and continuously learns industry knowledge.  

---

## 🛠️ <span style="color: #8e44ad;">System Architecture</span>  

The system employs a modular architecture leveraging large models and AGI:  

- 💬 **<span style="color: #16a085;">Interaction Module</span>**  
  Handles user interactions, processes input, and integrates local knowledge with web queries.  

- 🧠 **<span style="color: #34495e;">Memory Module</span>**  
  Manages short-term and long-term memories for smarter interactions.  

- 📖 **<span style="color: #e74c3c;">Knowledge Module</span>**  
  Supports dynamic loading, updating, and querying of knowledge base files.  

- 🌐 **<span style="color: #f1c40f;">WebSearch Module</span>**  
  Retrieves external data using web searches and large models (e.g., qwen2).  

- 🔗 **<span style="color: #d35400;">Tool Invocation Module</span>**  
  Extends functionality through external APIs for operations like weather reports and data analysis.  

---

## ⚙️ <span style="color: #2c3e50;">Installation and Configuration</span>  

### 🌍 <span style="color: #95a5a6;">Environmental Requirements</span>  

- 💻 **<span style="color: #1abc9c;">Operating System</span>**: Windows, macOS, Linux  
- 🐍 **<span style="color: #3498db;">Python Version</span>**: 3.6 or higher  
- 📦 **<span style="color: #e67e22;">Dependency Libraries</span>**:  

```bash
pip install ollama~=0.4.0
pip install docx~=0.2.4
pip install python-docx~=1.1.2
pip install pdfplumber~=0.11.2
```  

✨ Now you're all set! Happy coding! 🎉  