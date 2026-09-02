import streamlit as st
import random
import re

# Import all topic question lists
from topics.basic_networks import qa_basic_networks
from topics.network_security import qa_network_security
from topics.digital_forensics import qa_digital_forensics
from topics.laws_standards import qa_laws_standards
from topics.ai_ml_stats import qa_ai_ml_stats
from topics.scada_ot import qa_scada_ot
from topics.blockchain_crypto import qa_blockchain_crypto
from topics.data_science import qa_data_science
from topics.cloud_devsecops import qa_cloud_devsecops

# Page Configuration
st.set_page_config(
    page_title="Cyber & Tech Interview Prep Master",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = set()

if "random_drill" not in st.session_state:
    st.session_state.random_drill = None

# Custom CSS for Modern, Sleek UI
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #1E1B4B 0%, #312E81 50%, #4338CA 100%);
        border-radius: 16px;
        padding: 28px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(49, 46, 129, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .hero-title {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .hero-subtitle {
        font-size: 15px;
        color: #C7D2FE;
        font-weight: 400;
        line-height: 1.5;
    }

    /* Metric Pills */
    .metric-pill-container {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 14px;
    }
    .metric-pill {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(8px);
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 600;
        color: #EEF2FF;
        border: 1px solid rgba(255, 255, 255, 0.18);
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }

    /* Question Card */
    .q-badge {
        display: inline-block;
        background-color: #EEF2FF;
        color: #4338CA;
        font-size: 12px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    .q-title {
        font-size: 19px;
        font-weight: 700;
        color: #1E293B;
        line-height: 1.4;
        margin-bottom: 12px;
    }

    /* Section Boxes */
    .answer-lead {
        font-size: 15px;
        line-height: 1.65;
        color: #334155;
        margin-bottom: 12px;
    }
    .characteristics-box {
        background-color: #F8FAFC;
        border-left: 4px solid #6366F1;
        padding: 14px 18px;
        border-radius: 0 10px 10px 0;
        margin: 14px 0;
        font-size: 14.5px;
        color: #1E293B;
        line-height: 1.6;
    }
    .characteristics-header {
        font-weight: 700;
        color: #4338CA;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .example-box {
        background-color: #F0FDF4;
        border-left: 4px solid #10B981;
        padding: 14px 18px;
        border-radius: 0 10px 10px 0;
        margin: 14px 0 6px 0;
        font-size: 14.5px;
        color: #064E3B;
        line-height: 1.6;
    }
    .example-header {
        font-weight: 700;
        color: #047857;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
        border-right: 1px solid #E2E8F0;
    }
    .sidebar-stats {
        background: #FFFFFF;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        margin-bottom: 18px;
    }
    .stat-row {
        display: flex;
        justify-content: space-between;
        padding: 6px 0;
        font-size: 13.5px;
        color: #475569;
        border-bottom: 1px dashed #F1F5F9;
    }
    .stat-row:last-child {
        border-bottom: none;
    }
    .stat-val {
        font-weight: 700;
        color: #0F172A;
    }

    /* Drill Alert Box */
    .drill-banner {
        background: linear-gradient(135deg, #FFFBEB 0%, #FEF3C7 100%);
        border: 1px solid #FCD34D;
        border-radius: 12px;
        padding: 18px 22px;
        margin-bottom: 24px;
    }
</style>
""", unsafe_allow_html=True)

# Topics dictionary with category icons
topics = {
    "📊 Data Science": qa_data_science,
    "🧠 AI, Stats, ML & Maths": qa_ai_ml_stats,
    "☁️ Cloud Security & DevSecOps": qa_cloud_devsecops,
    "🌐 Basic Computer Networks": qa_basic_networks,
    "🛡️ Network & Cyber Security": qa_network_security,
    "🔍 Digital Forensics": qa_digital_forensics,
    "📜 Laws & Standards": qa_laws_standards,
    "🏭 SCADA / OT Security": qa_scada_ot,
    "⛓️ Blockchain & Cryptography": qa_blockchain_crypto,
}

total_all_questions = sum(len(q_list) for q_list in topics.values())

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    # App Branding
    col_logo, col_title = st.columns([1, 3])
    with col_logo:
        try:
            st.image("logo.png", width=65)
        except Exception:
            st.write("🧠")
    with col_title:
        st.markdown("<h3 style='margin:0; padding-top:4px; font-weight:800; color:#1E1B4B;'>Prep Master</h3>", unsafe_allow_html=True)
        st.caption("Interview Readiness Hub")

    st.markdown("<hr style='margin: 12px 0;'>", unsafe_allow_html=True)

    # Quick Statistics Box
    st.markdown(f"""
    <div class="sidebar-stats">
        <div style="font-size:12px; font-weight:700; color:#64748B; text-transform:uppercase; margin-bottom:8px;">Knowledge Base</div>
        <div class="stat-row"><span>📚 Topics</span><span class="stat-val">{len(topics)}</span></div>
        <div class="stat-row"><span>❓ Questions</span><span class="stat-val">{total_all_questions}</span></div>
        <div class="stat-row"><span>⭐ Saved Bookmarks</span><span class="stat-val">{len(st.session_state.bookmarks)}</span></div>
    </div>
    """, unsafe_allow_html=True)

    # Mode Selector
    st.markdown("##### 🎯 Practice Mode")
    study_mode = st.radio(
        "Select Mode",
        options=["📖 Study Mode (Full Q&A)", "🎯 Flashcard Mode (Recall Test)", "⭐ Saved Bookmarks"],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='margin: 12px 0;'>", unsafe_allow_html=True)

    # Topic Selector
    st.markdown("##### 📚 Select Topic")
    selected_topic = st.radio(
        "Choose a Topic",
        list(topics.keys()),
        label_visibility="collapsed"
    )

    st.markdown("<hr style='margin: 14px 0;'>", unsafe_allow_html=True)

    # Interactive Features: Random Drill
    st.markdown("##### ⚡ Quick Practice Drill")
    if st.button("🎲 Pop-Quiz Question", use_container_width=True, type="primary"):
        # Select random question either from current topic or any topic
        curr_list = topics[selected_topic]
        if curr_list:
            rand_q, rand_a = random.choice(curr_list)
            st.session_state.random_drill = {
                "topic": selected_topic,
                "question": rand_q,
                "answer": rand_a
            }
        st.rerun()

    if st.session_state.bookmarks and st.button("🗑️ Clear All Bookmarks", use_container_width=True):
        st.session_state.bookmarks.clear()
        st.rerun()

    st.markdown("---")
    st.caption("🎓 Cyber & Tech Interview Preparation")


# ==========================================
# ANSWER FORMATTING HELPER
# ==========================================
def format_interview_answer(raw_answer: str):
    """
    Parses structured answers (Direct Answer, Characteristics, Example)
    and formats them with distinct styled visual containers.
    Also handles standard plain text / numbered list answers cleanly.
    """
    has_direct = "**Direct Answer:**" in raw_answer
    has_chars = "**Key Characteristics:**" in raw_answer
    has_example = "**Example:**" in raw_answer

    if has_direct or has_chars or has_example:
        # Extract sections using regex
        direct_match = re.search(r"\*\*Direct Answer:\*\*\s*(.*?)(?=\*\*Key Characteristics:\*\*|\*\*Example:\*\*|$)", raw_answer, re.DOTALL)
        chars_match = re.search(r"\*\*Key Characteristics:\*\*\s*(.*?)(?=\*\*Example:\*\*|$)", raw_answer, re.DOTALL)
        example_match = re.search(r"\*\*Example:\*\*\s*(.*)", raw_answer, re.DOTALL)

        direct_text = direct_match.group(1).strip() if direct_match else ""
        chars_text = chars_match.group(1).strip() if chars_match else ""
        example_text = example_match.group(1).strip() if example_match else ""

        html_output = ""
        if direct_text:
            html_output += f"<div class='answer-lead'>{direct_text}</div>"

        if chars_text:
            formatted_chars = "<br>".join(
                [f"• {line.lstrip('•*- ')}" for line in chars_text.split("\n") if line.strip()]
            )
            html_output += f"""
            <div class='characteristics-box'>
                <div class='characteristics-header'>⚡ Key Characteristics & Mechanisms</div>
                {formatted_chars}
            </div>
            """

        if example_text:
            html_output += f"""
            <div class='example-box'>
                <div class='example-header'>💡 Interview Practical Example</div>
                {example_text}
            </div>
            """
        return html_output
    else:
        lines = [line.strip() for line in raw_answer.split("\n") if line.strip()]
        if len(lines) > 1 and all(lines[i][0].isdigit() for i in range(len(lines))):
            items = []
            for line in lines:
                clean_line = re.sub(r'^\d+\.\s*', '', line)
                items.append(f"<li style='margin-bottom:6px;'>{clean_line}</li>")
            formatted_items = "".join(items)
            return f"<ul style='margin: 8px 0 8px 20px; color:#334155; line-height:1.6;'>{formatted_items}</ul>"
        else:
            nl = "<br>"
            return f"<div class='answer-lead'>{raw_answer.replace(chr(10), nl)}</div>"


# ==========================================
# MAIN CONTENT AREA
# ==========================================

# Hero Banner
st.markdown(f"""
<div class="hero-banner">
    <div class="hero-title">
        <span>🧠</span> Cyber & Tech Interview Prep Hub
    </div>
    <div class="hero-subtitle">
        Master high-yield technical concepts with crisp, interview-calibrated answers, key traits, and practical examples.
    </div>
    <div class="metric-pill-container">
        <div class="metric-pill"><span>🎯</span> Active: {selected_topic}</div>
        <div class="metric-pill"><span>❓</span> {len(topics[selected_topic])} Topic Questions</div>
        <div class="metric-pill"><span>📚</span> {total_all_questions} Total Questions</div>
        <div class="metric-pill"><span>⭐</span> {len(st.session_state.bookmarks)} Bookmarked</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Random Drill Pop-up Banner if triggered
if st.session_state.random_drill:
    drill = st.session_state.random_drill
    st.markdown(f"""
    <div class="drill-banner">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-weight:800; color:#92400E; font-size:14px; text-transform:uppercase; letter-spacing:0.5px;">🎲 Rapid Interview Pop-Quiz</span>
            <span style="font-size:12px; font-weight:600; background:#FDE68A; color:#78350F; padding:2px 8px; border-radius:6px;">{drill['topic']}</span>
        </div>
        <div style="font-size:18px; font-weight:700; color:#78350F; margin: 10px 0 12px 0;">{drill['question']}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("👁️ Reveal Pop-Quiz Answer", expanded=False):
        st.markdown(format_interview_answer(drill['answer']), unsafe_allow_html=True)

    col_next, col_close = st.columns([1, 4])
    with col_next:
        if st.button("🔄 Another Question", key="drill_next"):
            curr_list = topics[selected_topic]
            if curr_list:
                rq, ra = random.choice(curr_list)
                st.session_state.random_drill = {"topic": selected_topic, "question": rq, "answer": ra}
                st.rerun()
    with col_close:
        if st.button("✖️ Dismiss Drill", key="drill_close"):
            st.session_state.random_drill = None
            st.rerun()
    st.markdown("<hr style='margin: 16px 0 24px 0;'>", unsafe_allow_html=True)


# Search Bar & Filter Controls
col_search, col_scope = st.columns([3, 1])
with col_search:
    search_query = st.text_input(
        "🔍 Search questions, concepts, or keywords:",
        placeholder="Type to filter e.g., 'Overfitting', 'PCA', 'Firewall', 'Isolation Forest', 'SQL'...",
        label_visibility="collapsed"
    )
with col_scope:
    search_scope = st.selectbox(
        "Search In",
        options=["Current Topic", "All Topics"],
        label_visibility="collapsed"
    )

# Determine Questions Dataset Based on Mode and Scope
if study_mode == "⭐ Saved Bookmarks":
    display_list = []
    for topic_name, q_list in topics.items():
        for q, a in q_list:
            if (topic_name, q) in st.session_state.bookmarks:
                display_list.append((topic_name, q, a))
elif search_query and search_scope == "All Topics":
    display_list = []
    for topic_name, q_list in topics.items():
        for q, a in q_list:
            display_list.append((topic_name, q, a))
else:
    display_list = [(selected_topic, q, a) for (q, a) in topics[selected_topic]]

# Apply Search Filter
if search_query:
    query = search_query.lower()
    filtered_list = [
        (top, q, a) for (top, q, a) in display_list
        if query in q.lower() or query in a.lower()
    ]
else:
    filtered_list = display_list

# Section Subtitle & Count
st.markdown(f"#### 📘 {selected_topic if study_mode != '⭐ Saved Bookmarks' else '⭐ Saved Bookmarks'}")

if search_query:
    st.caption(f"Showing **{len(filtered_list)}** matching question(s) for query *'{search_query}'*")
else:
    st.caption(f"Total: **{len(filtered_list)}** question(s)")

# Display Questions
if not filtered_list:
    if study_mode == "⭐ Saved Bookmarks":
        st.info("⭐ You haven't bookmarked any questions yet. Click the star button (⭐) on any question card to save it for quick revision!")
    else:
        st.warning("🔍 No questions matched your search criteria. Try a different keyword or toggle search scope.")
else:
    for idx, (top_name, question, answer) in enumerate(filtered_list, start=1):
        is_bookmarked = (top_name, question) in st.session_state.bookmarks

        with st.container(border=True):
            col_q, col_act = st.columns([0.92, 0.08])

            with col_q:
                st.markdown(f"""
                <span class='q-badge'>{top_name} • Q{idx}</span>
                <div class='q-title'>{question}</div>
                """, unsafe_allow_html=True)

            with col_act:
                star_label = "⭐" if is_bookmarked else "☆"
                star_help = "Remove bookmark" if is_bookmarked else "Save to bookmarks"
                if st.button(star_label, key=f"bm_{top_name}_{idx}_{hash(question)}", help=star_help):
                    if is_bookmarked:
                        st.session_state.bookmarks.remove((top_name, question))
                    else:
                        st.session_state.bookmarks.add((top_name, question))
                    st.rerun()

            # Display based on selected study mode
            formatted_ans = format_interview_answer(answer)

            if "Flashcard" in study_mode:
                with st.expander("👁️ Reveal Interview Answer & Examples", expanded=False):
                    st.markdown(formatted_ans, unsafe_allow_html=True)
            else:
                st.markdown(formatted_ans, unsafe_allow_html=True)

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #94A3B8; font-size: 13px; padding-bottom: 20px;'>
    🧠 <b>Cyber & Tech Interview Preparation Hub</b> • Crisp explanations, key characteristics, and real-world scenarios.
</div>
""", unsafe_allow_html=True)
