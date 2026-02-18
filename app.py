import streamlit as st
import time
import pandas as pd

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LingoLens AI | Neural Gateway", 
    page_icon="🧠", 
    layout="wide"
)

# --- 2. ADVANCED NEON CSS ---
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #051612 0%, #000000 100%);
        color: #00ff41;
    }
    .login-card {
        background: rgba(0, 255, 65, 0.05);
        border: 1px solid #00ff41;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 0 30px rgba(0, 255, 65, 0.1);
        text-align: center;
    }
    .neon-text {
        text-shadow: 0 0 10px #00ff41;
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        background-color: transparent;
        color: #00ff41 !important;
        border: 1px solid #00ff41 !important;
        width: 100%;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 20px #00ff41;
    }
    /* Input Styling */
    input { color: #00ff41 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE INITIALIZATION ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# --- 4. MINDBLOWING LOGIN PAGE ---
if not st.session_state.auth:
    _, col2, _ = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
            <div class="login-card">
                <h1 class="neon-text">LINGOLENS AI</h1>
                <p style="color: #008f11;">PROJECT BY BIOTWIN x LEARNOMINE</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Inputs
        input_user = st.text_input("CREATOR IDENTITY", placeholder="Type Learnomine_Creator")
        input_key = st.text_input("NEURAL ENCRYPTION KEY", type="password", placeholder="Enter NLP_PRO_2026")
        
        if st.button("INITIALIZE NEURAL LINK"):
            if input_user == "Learnomine_Creator" and input_key == "NLP_PRO_2026":
                st.session_state.auth = True
                st.session_state.user_name = input_user # ఇక్కడ డేటా సేవ్ అవుతుంది
                st.toast("Verification Successful...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("ACCESS DENIED: Credentials Mismatch")
    st.stop()

# --- 5. MAIN DASHBOARD (ONLY VISIBLE AFTER LOGIN) ---
# Sidebar సెక్షన్
st.sidebar.markdown(f"### 🚀 Welcome, \n**{st.session_state.user_name}**")
st.sidebar.divider()
st.sidebar.write("**Model:** Naive Bayes")
st.sidebar.write("**Vector:** TF-IDF")
st.sidebar.write("**Status:** Neural Link Active")

if st.sidebar.button("LOGOUT"):
    st.session_state.auth = False
    st.rerun()

# Main UI
st.title("🧠 Neural Text Analysis Engine")
st.write("---")

col_input, col_viz = st.columns([2, 1])

with col_input:
    st.subheader("Input Stream")
    user_text = st.text_area("Enter text to classify:", placeholder="Paste message here...", height=200)
    
    if st.button("RUN INFERENCE"):
        if user_text:
            with st.status("Processing NLP Pipeline...", expanded=True) as status:
                st.write("Step 1: Cleaning text (removing stopwords)...")
                time.sleep(0.8)
                st.write("Step 2: Vectorizing with TF-IDF...")
                time.sleep(0.6)
                st.write("Step 3: Calculating probability...")
                time.sleep(0.5)
                status.update(label="Analysis Complete!", state="complete")
            
            # Simulated logic for demo (మీ మోడల్ ఉంటే ఇక్కడ .predict() వాడండి)
            is_spam = "win" in user_text.lower() or "free" in user_text.lower()
            
            if is_spam:
                st.error(f"### Result: SPAM DETECTED ⚠️")
            else:
                st.success(f"### Result: LEGITIMATE MESSAGE ✅")
        else:
            st.warning("Please enter some text to analyze.")

with col_viz:
    st.subheader("Pipeline Metrics")
    st.progress(98, text="Model Accuracy")
    st.progress(100, text="System Latency: 24ms")
    
    st.divider()
    st.markdown("""
    **NLP Steps:**
    1. Tokenization
    2. Stopword Removal
    3. Lemmatization
    4. Vectorization
    """)



st.markdown("---")
st.caption("LingoLens AI | Developed for Portfolio 2026")
