import streamlit as st
from src.data_loader import load_documents, create_chunks
from src.retriever import get_retriever
from src.chatbot import get_chain

# ─── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Pakistani Legal AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

[data-testid="stSidebar"] { background-color: #0f1b2d; }
[data-testid="stSidebar"] * { color: #e8eaf6 !important; }
[data-testid="stSidebar"] .stButton > button {
    background-color: #1a2e4a; border: 1px solid #2e4a6e;
    color: #e8eaf6 !important; border-radius: 8px;
    width: 100%; text-align: left; padding: 0.5rem 1rem;
    margin-bottom: 4px;
}
.user-bubble {
    background: #1a2e4a; color: #e8eaf6;
    border-radius: 18px 18px 4px 18px;
    padding: 12px 18px; margin: 8px 0;
    max-width: 80%; margin-left: auto; font-size: 15px; line-height: 1.6;
}
.bot-bubble {
    background: #f5f7fa; color: #1a1a2e;
    border-radius: 18px 18px 18px 4px;
    padding: 14px 18px; margin: 8px 0;
    max-width: 85%; border-left: 3px solid #c8a951;
    font-size: 15px; line-height: 1.7;
}
.app-header {
    background: linear-gradient(135deg, #0f1b2d 0%, #1a2e4a 100%);
    color: white; padding: 1.5rem 2rem; border-radius: 12px;
    margin-bottom: 1.5rem; display: flex; align-items: center; gap: 1rem;
}
.stat-card {
    background: #f5f7fa; border-radius: 10px;
    padding: 12px 16px; text-align: center;
}
.stat-num { font-size: 22px; font-weight: 700; color: #1a2e4a; }
.stat-label { font-size: 11px; color: #6b7280; margin-top: 2px; }
.empty-state { text-align: center; padding: 3rem 2rem; color: #8ba7cc; }
.urdu-text { font-family: 'Noto Nastaliq Urdu', serif; direction: rtl; font-size: 16px; line-height: 2; }
</style>
""", unsafe_allow_html=True)


# ─── Session State Init ────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ""
if "ready" not in st.session_state:
    st.session_state.ready = False
if "chain" not in st.session_state:
    st.session_state.chain = None


# ─── Load Backend (ONLY ONCE) ─────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def load_backend():
    docs = load_documents()
    parent_chunks, child_chunks = create_chunks(docs)
    retriever = get_retriever(child_chunks)
    chain = get_chain(retriever)
    return chain

if not st.session_state.ready:
    with st.spinner("⚖️ Loading legal database... please wait"):
        try:
            chain = load_backend()
            st.session_state.chain = chain
            st.session_state.ready = True
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()


# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚖️ Pakistani Legal AI")
    st.markdown("---")
    st.success("✅ Legal database ready")
    st.markdown("---")
    st.markdown("**📚 Covered Laws**")
    laws = [
        "🏛️ Constitution of Pakistan",
        "⚖️ Pakistan Penal Code",
        "🔒 PECA 2016",
        "👩 Harassment Act",
        "👨‍👩‍👧 Family Laws",
        "💍 Child Marriage Laws",
        "🩸 Honor Killing Laws",
        "👷 Labour Laws",
        "♀️ Women Rights",
        "🌍 Human Rights",
        "🏠 Domestic Violence",
        "📝 Divorce Laws",
    ]
    for law in laws:
        st.markdown(f"<small>{law}</small>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat_history = ""
        st.rerun()
    st.markdown("""
    <small style="color: #8ba7cc;">
    ⚠️ For informational purposes only.<br>
    Always consult a qualified lawyer.
    </small>
    """, unsafe_allow_html=True)


# ─── Main Area ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <span style="font-size: 40px;">⚖️</span>
    <div>
        <p style="font-size:26px; font-weight:700; color:#fff; margin:0;">Pakistani Legal AI Assistant</p>
        <p style="font-size:13px; color:#8ba7cc; margin:2px 0 0;">Ask about Pakistani law in English or Urdu • پاکستانی قانون کے بارے میں سوال کریں</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-card"><div class="stat-num">12</div><div class="stat-label">Laws Covered</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-card"><div class="stat-num">666</div><div class="stat-label">Legal Chunks</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-card"><div class="stat-num">2</div><div class="stat-label">Languages</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-card"><div class="stat-num">70B</div><div class="stat-label">LLM Parameters</div></div>', unsafe_allow_html=True)

st.markdown("")

# ─── Quick Questions ───────────────────────────────────────────────────────────
QUICK_QUESTIONS = [
    "What is the punishment for murder under PPC?",
    "What are a woman's rights in divorce?",
    "How to file a harassment complaint?",
    "What does PECA say about cybercrime?",
    "What is the legal age for marriage?",
    "What are labor rights in Pakistan?",
]

if not st.session_state.messages:
    st.markdown("**💡 Try asking:**")
    cols = st.columns(3)
    for i, q in enumerate(QUICK_QUESTIONS):
        with cols[i % 3]:
            if st.button(q, key=f"quick_{i}", use_container_width=True):
                st.session_state["pending_q"] = q

# ─── Chat History ──────────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown("""
    <div class="empty-state">
        <div style="font-size:48px;">⚖️</div>
        <p style="font-size:18px; font-weight:600; color:#1a2e4a; margin:8px 0 0;">Your Legal Assistant is Ready</p>
        <p style="font-size:14px; color:#6b7280; margin-top:8px;">Ask any question about Pakistani law below.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div style="display:flex; justify-content:flex-end; margin:8px 0;">
                <div class="user-bubble">{msg["content"]}</div>
            </div>""", unsafe_allow_html=True)
        else:
            urdu_chars = sum(1 for c in msg["content"] if '\u0600' <= c <= '\u06FF')
            is_urdu = urdu_chars > len(msg["content"]) * 0.3
            css = "bot-bubble urdu-text" if is_urdu else "bot-bubble"
            st.markdown(f'<div class="{css}">{msg["content"]}</div>', unsafe_allow_html=True)

# ─── Input ─────────────────────────────────────────────────────────────────────
st.markdown("---")
input_col, btn_col = st.columns([6, 1])
with input_col:
    user_input = st.text_input(
        "question",
        placeholder="e.g. What are my rights as a tenant in Pakistan?",
        label_visibility="collapsed",
        key="user_input",
    )
with btn_col:
    send = st.button("Send ➤", type="primary", use_container_width=True)

# Handle quick question
if "pending_q" in st.session_state:
    user_input = st.session_state.pop("pending_q")
    send = True

# ─── Process Query ─────────────────────────────────────────────────────────────
if send and user_input.strip():
    query = user_input.strip()
    st.session_state.messages.append({"role": "user", "content": query})

    with st.spinner("⚖️ Searching legal database..."):
        try:
            answer = st.session_state.chain({
                "question": query,
                "chat_history": st.session_state.chat_history
            })
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.session_state.chat_history += f"\nHuman: {query}\nAssistant: {answer[:400]}\n"
            lines = st.session_state.chat_history.split("\n")
            if len(lines) > 18:
                st.session_state.chat_history = "\n".join(lines[-18:])
        except Exception as e:
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"⚠️ Error: {str(e)}\n\nPlease try again."
            })
    st.rerun()