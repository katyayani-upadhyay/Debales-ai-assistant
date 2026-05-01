import streamlit as st
from graph import build_graph

# build app
app = build_graph()

st.set_page_config(page_title="Debales AI Assistant", page_icon="🤖")

st.title("🤖 Debales AI Assistant")
st.write("Ask anything about Debales AI or general AI topics.")

# session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# user input
user_input = st.text_input("You:")

if user_input:
    result = app.invoke({"query": user_input})
    response = result["response"]

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# display chat
for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")