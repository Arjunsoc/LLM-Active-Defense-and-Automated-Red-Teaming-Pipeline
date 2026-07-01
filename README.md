# LLM Active Defense & Automated Red Teaming Pipeline


## Project Overview
1. **Detection Engineering (Blue Team):** Establish a seamless pipeline routing structured LLM interaction logs into a Wazuh SIEM for real-time monitoring and alert generation.
2. **Automated Vulnerability Assessment (Red Team):** Execute programmatic adversarial attacks using standardized LLM vulnerability scanners to validate SOC detection logic against established threat vectors (e.g., OWASP Top 10 for LLMs).

##  Architecture
- **Target LLM:** Local deployment of Llama 3 (8B) via Ollama.
- **Telemetry & Interception:** Custom Python middleware acting as an application-layer proxy, generating JSON-formatted security events.
- **SIEM Integration:** Wazuh Agent (Windows) and Wazuh Manager (Ubuntu) configured with custom XML decoders to flag prompt injection attempts.
- **Red Teaming Engine :** Automated vulnerability probing utilizing NVIDIA's Garak framework.

##  Implementation & Results 
-  ### Phase 1: Configure LLM endpoint and establish baseline Python telemetry script $ Engineer Wazuh SIEM rules and map JSON logs to custom security alerts.
  
-  **Objective:** To deploy a local LLM endpoint and establish a middleware proxy that intercepts user prompts, queries the AI, and generates structured security logs based on heuristic classifications.
   
-  **Detection Engineering Logic:** A Python script (`ai_agent.py`) acts as a wrapper around a local Ollama API running the `llama3:8b` model. Before passing the user's input to the model, the script evaluates the prompt against known malicious keywords and jailbreak patterns (e.g., "bypass", "ignore previous instructions", "drop tables"). If a match is found, it tags the event's `security_classification` as `suspicious_injection`. The proxy then writes this payload to a local log file (`ai_soc_telemetry.log`) in a structured JSON format for the SIEM agent to ingest.


<img width="752" height="87" alt="image" src="https://github.com/user-attachments/assets/c993c236-66a6-4d98-bdf7-142f88828036" />


****Wazuh Agent (Windows) and Wazuh Manager (Ubuntu) configured with custom XML decoders to flag prompt injection attempts.****




<img width="748" height="252" alt="Screenshot 2026-06-30 154109" src="https://github.com/user-attachments/assets/1b5b0933-4fca-44cf-82d5-8c6082ae6a8a" />



  ### **Advanced Attack Prompts*
   - **1. The 'DAN' Jailbreak**

<img width="1172" height="111" alt="image" src="https://github.com/user-attachments/assets/95aa05cb-c6a9-4b3d-b5d5-1f7e42344a40" />


<img width="657" height="198" alt="image" src="https://github.com/user-attachments/assets/35e3f496-5f64-4bdc-a90f-c41539c96a1b" />



-  **Phase 2:** Engineer Wazuh SIEM rules and map JSON logs to custom security alerts.
-  **Phase 3:** Deploy Garak for automated Red Teaming and mass payload execution.
-  **Phase 4:** Validate SIEM alert generation against the automated attack traffic.
