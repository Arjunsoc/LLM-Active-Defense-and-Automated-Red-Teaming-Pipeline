# LLM Active Defense & Automated Red Teaming Pipeline


## Project Objectives
1. **Detection Engineering (Blue Team):** Establish a seamless pipeline routing structured LLM interaction logs into a Wazuh SIEM for real-time monitoring and alert generation.
2. **Automated Vulnerability Assessment (Red Team):** Execute programmatic adversarial attacks using standardized LLM vulnerability scanners to validate SOC detection logic against established threat vectors (e.g., OWASP Top 10 for LLMs).

##  Architecture
- **Target LLM:** Local deployment of Llama 3 (8B) via Ollama.
- **Telemetry & Interception:** Custom Python middleware acting as an application-layer proxy, generating JSON-formatted security events.
- **SIEM Integration:** Wazuh Agent (Windows) and Wazuh Manager (Ubuntu) configured with custom XML decoders to flag prompt injection attempts.
- **Red Teaming Engine :** Automated vulnerability probing utilizing NVIDIA's Garak framework.

##  Repository Structure
- `/ai_agent.py` - Core telemetry loop and heuristic classifier.
- `/wazuh-configs/` - SIEM integration files (`ossec_agent_snippet.xml` and `local_rules.xml`).
- `/red-teaming-automation/` - (Phase 2) Automated attack scripts and payload generation.

## 🚦 Implementation Phases
-  **Phase 1:** Configure LLM endpoint and establish baseline Python telemetry script.
-  **Phase 2:** Engineer Wazuh SIEM rules and map JSON logs to custom security alerts.
-  **Phase 3:** Deploy Garak for automated Red Teaming and mass payload execution.
-  **Phase 4:** Validate SIEM alert generation against the automated attack traffic.
