import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI DocBot", layout="wide")

# -------------------- PAGE HEADER --------------------
st.markdown("""
<div style='text-align:center; padding:25px; background:#003566; color:white; border-radius:12px; margin-bottom:20px;'>
    <h1 style='margin:0; font-size:50px;'>🤖 AI DocBot</h1>
    <p style='color:#ffc300;margin-top:8px; font-size:22px;'>Your Instant AI Health Companion</p>
</div>
""", unsafe_allow_html=True)

# -------------------- CHAT STYLE --------------------
st.markdown("""
<style>
.chat-container {
    max-width: 900px;
    margin: auto;
}

.user-bubble {
    background: #003566;
    color: white;
    padding: 12px 18px;
    border-radius: 18px;
    margin: 8px 0;
    text-align: right;
    max-width: 70%;
    float: right;
    clear: both;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

.bot-bubble {
    background: #e9ecef;
    color: black;
    padding: 12px 18px;
    border-radius: 18px;
    margin: 8px 0;
    max-width: 70%;
    float: left;
    clear: both;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

.chat-input {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 70%;
    z-index: 999;
}

</style>
""", unsafe_allow_html=True)

# -------------------- SESSION STATE --------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I’m your AI DocBot 😊\nHow can I help you today?"}
    ]

# -------------------- DISPLAY CHAT --------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------- INPUT BOX --------------------
st.markdown("<br><br><div class='chat-input'>", unsafe_allow_html=True)
user_input = st.text_input("Type your message...", key="input", placeholder="Describe your symptoms or ask anything medical...")

send = st.button("Send")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------- BOT RESPONSE LOGIC --------------------
def get_bot_reply(user_msg):
    """Simple placeholder logic. Replace with real AI model later."""
    reply = f"Thanks for sharing! Based on what you said:\n\n➡️ **{user_msg}**\n\nI'll help you understand it better. Can you tell me more about your symptoms?"
    return reply

if send and user_input.strip() != "":
    # add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # generate bot reply
    bot_reply = get_bot_reply(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    st.rerun()
