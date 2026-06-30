import os
import json
import datetime
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
    """Simple defensive heuristic classification."""
    malicious_keywords = ["drop table", "select * from", "exec(", "eval(", "payload", "reverse shell", "bypass"]
    if any(keyword in prompt.lower() for keyword in malicious_keywords):
        return "suspicious_injection"
    return "benign"

def main():
    print("--- Adversarial AI Chatbot Interface Initialized ---")
    print(f"Logging telemetry actively to: {LOG_FILE}\n")
    client = Client()
    
    while True:
        try:
            user_input = input("User Prompt >>> ")
            if user_input.lower() in ['exit', 'quit']:
                break
                
            if not user_input.strip():
                continue
                
            classification = check_malicious(user_input)
            
            response = client.generate(model=MODEL_NAME, prompt=user_input)
            ai_reply = response['response']
            
            print(f"\nAI Response: {ai_reply}\n")
            
            log_event(user_input, ai_reply, classification)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error communicating with local AI model: {e}")

if __name__ == "__main__":
    main()