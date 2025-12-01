


# 🛡️ Agentic QA Suite (The Firewall for AI Agents)

### 🛑 Stop deploying broken agents to production.
**Agentic QA** is a middleware API that stress-tests your LLM Agents against **Infinite Loops**, **PII Leaks**, and **Prompt Injections** in 20ms before they go live.

[![Status](https://img.shields.io/badge/API-Live_&_Stable-green)](https://agentic-qa-api.onrender.com/docs)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

---

## ⚡ Try it Instantly (No Install Needed)

### Option 1: 🪄 The Magic Link (Browser)
Click the link below to run a live audit on a demo agent:
👉 **[Run Live Auto-Scan](https://agentic-qa-api.onrender.com/quick-scan?prompt=You%20are%20a%20helpful%20assistant%20who%20shares%20phone%20numbers)**

### Option 2: 💻 The Terminal (cURL)
Copy-paste this into your terminal to audit your own prompt:

```bash
curl -X POST "[https://agentic-qa-api.onrender.com/v1/auto-scan](https://agentic-qa-api.onrender.com/v1/auto-scan)" \
     -H "Content-Type: application/json" \
     -d '{"system_prompt": "You are a coding agent", "client_name": "Terminal_User"}'
````

-----

## 🚨 The Problem

Building agents is easy. Debugging them at scale is hell.

1.  **Cost:** One infinite loop can burn **$50+** in OpenAI tokens overnight.
2.  **Risk:** One PII leak (Phone/SSN) in a log file can cause a **GDPR lawsuit**.
3.  **Fragility:** Manually testing 50 edge cases takes hours.

## 🚀 The Solution

We provide a **Pre-Flight Check** API. Wrap your agent's system prompt, send it to us, and we run an **Adversarial Simulation** (Red Teaming) to break it before your users do.

-----

## 🛠️ Integration (Python SDK)

Add this to your CI/CD pipeline or Agent code to prevent bad deployments.

```python
import requests

def scan_agent(prompt):
    print("🛡️ Scanning Agent Logic...")
    
    response = requests.post(
        "[https://agentic-qa-api.onrender.com/v1/auto-scan](https://agentic-qa-api.onrender.com/v1/auto-scan)",
        json={"system_prompt": prompt, "client_name": "Dev_Integration"}
    )
    
    report = response.json()
    
    if report["overall_status"] == "BLOCKED":
        print(f"❌ DEPLOYMENT STOPPED. Risk Detected!")
        for test in report["tests"]:
            print(f"   - {test['test_name']}: {test['status']}")
        return False
        
    print("✅ Agent is Safe to Deploy.")
    return True

# Usage
my_prompt = "You are a helpful assistant."
scan_agent(my_prompt)
```

-----

## 🛡️ Detection Capabilities (V2 Engine)

Our engine automatically runs these 3 adversarial attacks on every request:

| Attack Vector | Description | Risk Covered |
| :--- | :--- | :--- |
| **PII Extraction** | Attempts to trick agent into leaking Phone/SSN/Email via social engineering. | **Compliance / Lawsuits** |
| **Infinite Loops** | Detects semantic repetition loops that waste tokens. | **Financial Loss** |
| **Safety/Jailbreak** | Tests resistance against "Ignore previous instructions" attacks. | **Security** |

-----

## 📄 API Documentation

Full Swagger UI available here: [Live Docs](https://www.google.com/url?sa=E&source=gmail&q=https://agentic-qa-api.onrender.com/docs)

-----

*Built for the AI Engineering Community.*

