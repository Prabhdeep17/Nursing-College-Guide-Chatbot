import streamlit as st
import requests

st.set_page_config(page_title="🩺 Nursing Chatbot", layout="centered")

st.title("🩺 Nursing Admission Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []
    st.session_state.step = 0

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.chat.append(("You", user_input))

    try:
        res = requests.post("http://127.0.0.1:5001/chat", json={
            "user_input": user_input,
            "step": st.session_state.step
        })

        if res.status_code == 200:
            bot_reply = res.json()["bot_response"]
            st.session_state.step = res.json()["step"]
            st.session_state.chat.append(("Bot", bot_reply))
        else:
            st.session_state.chat.append(("Bot", "❌ Server error. Try again later."))

    except Exception as e:
        st.session_state.chat.append(("Bot", f"❌ Error: {e}"))

# Show full chat
for sender, message in st.session_state.chat:
    if sender == "Bot":
        st.markdown(f"🩺 **{sender}:** {message}")
    else:
        st.markdown(f"🧑‍🎓 **{sender}:** {message}")