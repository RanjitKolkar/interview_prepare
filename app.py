import streamlit as st

# Import all topic question lists
from topics.basic_networks import qa_basic_networks
from topics.network_security import qa_network_security
from topics.digital_forensics import qa_digital_forensics
from topics.laws_standards import qa_laws_standards
from topics.ai_ml_stats import qa_ai_ml_stats
from topics.scada_ot import qa_scada_ot
from topics.blockchain_crypto import qa_blockchain_crypto

st.set_page_config(page_title="Cyber Interview Prep", layout="wide")

# Display logo
st.image("logo.png", width=100)  # adjust width as needed
st.title("🧠 Cyber Interview Preparation ")

# Material Design-Inspired CSS
st.markdown("""
<style>
    /* Root layout */
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
        background-color: #f5f7fa;
    }

    .question-box {
        background-color: #ffffff;
        padding: 20px 24px;
        margin-bottom: 20px;
        border-radius: 12px;
        border-left: 6px solid #6200ea;
        box-shadow: 0 3px 8px rgba(0,0,0,0.08);
        transition: all 0.2s ease-in-out;
    }

    .question-box:hover {
        box-shadow: 0 6px 20px rgba(98, 0, 234, 0.12);
    }

    .question {
        font-weight: 600;
        color: #1a237e;
        font-size: 18px;
    }

    .answer {
        margin-top: 10px;
        color: #37474f;
        font-size: 16px;
        line-height: 1.6;
    }

    .sidebar .sidebar-content {
        background-color: #eceff1;
    }

    /* Sidebar radio buttons */
    section[data-testid="stSidebar"] .stRadio > div {
        background-color: #f1f3f4;
        border-radius: 8px;
        padding: 10px;
        color: #212121;
    }

    section[data-testid="stSidebar"] .stRadio > div label {
        font-weight: 500;
        color: #263238;
    }
</style>
""", unsafe_allow_html=True)

# Topics dictionary
topics = {
    "Basic Computer Networks": qa_basic_networks,
    "Network Security & Cyber Security": qa_network_security,
    "Digital Forensics": qa_digital_forensics,
    "Laws & Standards": qa_laws_standards,
    "AI, Stats, ML, Maths": qa_ai_ml_stats,
    "SCADA/OT Security": qa_scada_ot,
    "Blockchain & Cryptography": qa_blockchain_crypto,
}

# Sidebar navigation
st.sidebar.title("📚 Topics")
selected_topic = st.sidebar.radio("Choose a Topic", list(topics.keys()))

st.subheader(f"📘 {selected_topic}")
qa_list = topics[selected_topic]

# Display Q&A
if not qa_list:
    st.info("🚧 This section is under development. Check back soon!")
else:
    for idx, (question, answer) in enumerate(qa_list, start=1):
        st.markdown(f"""
        <div class='question-box'>
            <div class='question'>{idx}. {question}</div>
            <div class='answer'>{answer}</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("🎓 Developed for NFSU Cyber Interview Prep")
