# <span style="color: #3498db;">OmniAI</span>

<div align="center">

[简体中文](README_CN.md) / [繁体中文](README_TC.md) / English

</div>


## <span style="color: #2ecc71;">Project Overview</span>
This project constructs an intelligent assistant leveraging large model technologies (such as the <span style="color: #e74c3c;">Ollama model framework</span>) and Artificial General Intelligence (AGI) technologies. The intelligent assistant features multiple capabilities including short-term and long-term memory, tool invocation, planning, and execution. It aims to enhance the work efficiency of front-line workers and equip them with the competencies of industry experts.
By integrating advanced natural language processing technologies, the intelligent assistant can deliver precise operational guidance, business decision support, and problem-solving solutions tailored to specific fields. Its design facilitates adaptability to a variety of industry application scenarios, thereby streamlining work processes and reducing operational complexity.
> <span style="color: #f1c40f;">**Note**</span>: This product is currently in the testing phase, and the content of the provided knowledge base is intended for testing purposes only. When deploying the product in a live environment, users will need to incorporate industry-specific knowledge as required.
## <span style="color: #9b59b6;">Core Functions</span>
- **<span style="color: #1abc9c;">Industry Expert Capability</span>**: The intelligent assistant possesses professional knowledge in specific industries and is capable of addressing industry-related queries.
- **<span style="color: #3498db;">Short-term and Long-term Memory</span>**: The assistant can recall users' short-term inputs (e.g., the content of specific questions) and long-term information (e.g., users' common operational habits or needs), enhancing the efficiency and intelligence of subsequent interactions.
- **<span style="color: #e67e22;">Tool Invocation</span>**: The assistant can leverage external tools for operations such as web searches and document retrieval, broadening the scope and accuracy of its responses.
- **<span style="color: #95a5a6;">Planning and Execution</span>**: It offers basic task management and execution capabilities to help users effectively plan and carry out work tasks.
- **<span style="color: #f39c12;">Automated Decision-making</span>**: Utilizing large model technologies, the assistant can not only provide information but also autonomously generate solutions based on user needs and execute related tasks.
- **<span style="color: #2c3e50;">Document and Knowledge Base Management</span>**: The intelligent assistant can process and extract information from local documents (e.g., `.docx` and `.pdf` files), automatically update the local knowledge base, and continuously enrich its industry knowledge.
## <span style="color: #8e44ad;">System Architecture</span>
The system, grounded in large model technologies and AGI, employs a modular architecture. The modules are as follows:
- **<span style="color: #16a085;">Interaction Module</span>**: Handles user interactions, processes user input, and matches it against the local knowledge base and document content. When a response is not available locally, it initiates web queries using external large models.
- **<span style="color: #34495e;">Memory Module</span>**: Manages short-term and long-term memories. Short-term memory captures the most recent user inputs, while long-term memory retains more enduring information, enhancing the system's intelligence.
- **<span style="color: #e74c3c;">Knowledge Module</span>**: Manages and queries local knowledge base files, supporting dynamic loading, updating, and storage of knowledge.
- **<span style="color: #f1c40f;">WebSearch Module</span>**: Facilitates web searches, integrates external large models (such as qwen2), and retrieves external data to answer questions.
- **<span style="color: #d35400;">Tool Invocation Module</span>**: Extends functionality by invoking external APIs and tools, such as weather reports and supply chain data analysis.
## <span style="color: #2c3e50;">Installation and Configuration</span>
### <span style="color: #95a5a6;">Environmental Requirements</span>
- **<span style="color: #1abc9c;">Operating System</span>**: Compatible with Windows, macOS, Linux.
- **<span style="color: #3498db;">Python Version</span>**: 3.6 or higher.
- **<span style="color: #e67e22;">Dependency Libraries</span>**:
  ```bash
  pip install ollama~=0.4.0
  pip install docx~=0.2.4
  pip install python-docx~=1.1.2
  pip install pdfplumber~=0.11
