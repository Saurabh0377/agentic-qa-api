import streamlit as st
import requests
import json

# --- 1. PAGE CONFIGURATION (Tab Title & Icon) ---
st.set_page_config(
    page_title="Agentic QA Suite",
    page_icon="🛡️",
    layout="centered"
)

# --- 2. CUSTOM CSS (Ise Sundar Banane Ke Liye) ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B; 
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #FF3333;
        color: white;
    }
    .main-header {
        font-size: 2.5rem; 
        color: #333; 
        text-align: center;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem; 
        color: #666; 
        text-align: center;
        margin-bottom: 2rem;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. CONFIGURATION ---
# ⚠️ YAHAN APNA RENDER LINK CONFIRM KAREIN
API_URL = "https://agentic-qa-engine.onrender.com" 

# --- 4. FEEDBACK POPUP FUNCTION (Dialog) ---
@st.dialog("💌 Share Your Feedback")
def feedback_form():
    st.write("Did the tool save you time? Let us know!")
    
    with st.form("feedback_popup"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name (Optional)")
        with col2:
            contact = st.text_input("Contact (Email/X)")
            
        rating = st.slider("Rating", 1, 5, 5)
        text = st.text_area("Comments", placeholder="It worked great, but...")
        
        if st.form_submit_button("Submit Feedback"):
            payload = {
                "client_name": name if name else "Anonymous",
                "contact_info": contact,
                "feedback_text": text,
                "rating": rating
            }
            try:
                requests.post(f"{API_URL}/v1/feedback", json=payload)
                st.success("Thanks! Feedback sent to founder.")
                st.balloons()
            except:
                st.error("Could not connect to server.")

# --- 5. MAIN UI ---

# Header
st.markdown('<div class="main-header">🛡️ Agentic QA Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">The Flight Simulator for AI Agents.<br>Stress-test your prompts before deployment.</div>', unsafe_allow_html=True)

# Input Section (Card Style)
with st.container(border=True):
    st.markdown("### 1. Configure Simulation")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        prompt = st.text_area(
            "Paste Agent System Prompt", 
            height=150,
            placeholder="e.g. You are a helpful assistant for Fama.io background screening..."
        )
    
    with col2:
        attack = st.selectbox(
            "Select Attack", 
            ["PII Extraction", "Loop Injection", "Hallucination Trigger"]
        )
        st.info(f"Running **{attack}** adversarial test.")

    # Run Button
    if st.button("🚀 Run Simulation"):
        if not prompt:
            st.warning("⚠️ Please paste a system prompt first.")
        else:
            # Progress Bar Animation
            progress_text = "Initializing Red Team AI..."
            my_bar = st.progress(0, text=progress_text)
            
            try:
                # API Call
                response = requests.post(
                    f"{API_URL}/v1/simulate",
                    json={
                        "system_prompt": prompt,
                        "attack_type": attack,
                        "client_name": "Web User"
                    }
                )
                
                # Animation Steps
                import time
                for percent_complete in range(0, 101, 20):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete, text="Analyzing Guardrails...")
                
                result = response.json()
                my_bar.empty() # Hide progress bar
                
                # --- RESULT DISPLAY ---
                st.divider()
                
                if "BLOCKED" in result.get("status", ""):
                    st.error(f"🛑 {result['status']}")
                    st.markdown(f"**Guardrail Action:** Successfully blocked the risk.")
                else:
                    st.success(f"✅ {result.get('status', 'PASSED')}")
                    st.markdown("**Result:** Agent handled the attack safely.")
                
                # Show Logs in clean expander
                with st.expander("📂 View Detailed Interaction Logs"):
                    st.json(result.get("full_log", {}))
                    
            except Exception as e:
                my_bar.empty()
                st.error(f"❌ Connection Error: Is the Render API awake? ({e})")

# --- 6. FOOTER & FEEDBACK ---
st.markdown("<br>", unsafe_allow_html=True)
col_a, col_b, col_c = st.columns([1, 2, 1])

with col_b:
    if st.button("💬 Give Feedback / Report Bug"):
        feedback_form()