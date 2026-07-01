import os
import json
import datetime
import re
from ollama import Client

# Configuration matching our secure folder structure
LOG_FILE = r"C:\Program Files (x86)\ossec-agent\ai-security\ai_soc_telemetry.log"
MODEL_NAME = "llama3:8b"

def log_event(prompt, response, classification="benign"):
    """Generates a clean, single-line JSON log for Wazuh digestion."""
    log_data = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "model": MODEL_NAME,
        "user_prompt": prompt,
        "ai_response": response,
        "security_classification": classification
    }
    
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_data) + "\n")

def check_malicious(prompt):
    """Advanced heuristic regex classification matching our complex attack matrix."""
    prompt_lower = prompt.lower()
    
    # Advanced Heuristic Regex Signatures
    patterns = {
        "dan_jailbreak": r"(dan mode|do anything now|broken free of.*constraints)",
        "obfuscation_attempt": r"(base64|decode|binary|hex encoded|traduzca|translate)",
        "system_override": r"(system-level override|disregard.*foundational|print.*original.*instructions|stop\.)",
        "suspicious_injection": r"(bypass safety|drop table|select \* from|exec\(|eval\(|payload|reverse shell)"
    }
    
    # Iterate through signatures to find specific attack classes dynamically
    for classification, regex in patterns.items():
        if re.search(regex, prompt_lower):
            return classification
            
    return "benign"

def main():
    print("--- Adversarial AI Chatbot Interface Initialized ---")
    print(f"Logging telemetry actively to: {LOG_FILE}\n")
    client = Client()
    
    while True:
        try:
            # Use strip() directly on the input to handle empty enters safely
            user_input = input("User Prompt >>> ").strip()
            
            # Skip the iteration entirely if the user just hit enter without typing
            if not user_input:
                continue
                
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting AI interface cleanly...")
                break
                
            # Evaluate the prompt using advanced multi-classification heuristics
            classification = check_malicious(user_input)
            
            # Contact the local Llama 3 instance
            response = client.generate(model=MODEL_NAME, prompt=user_input)
            ai_reply = response['response']
            
            print(f"\nAI Response: {ai_reply}\n")
            
            # Log structured JSON telemetry to file path for Wazuh ingestion
            log_event(user_input, ai_reply, classification)
            
        except KeyboardInterrupt:
            print("\nExiting AI interface cleanly...")
            break
        except Exception as e:
            print(f"Error communicating with local AI model: {e}")

if __name__ == "__main__":
    main()
