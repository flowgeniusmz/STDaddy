import streamlit as st



def initialize_session_state_messages():
    initial_assistant_message = {"role": "assistant", "content": "I am your FlowGenius Assistant. How may I help you?"}
    if "messages_webexplorer_1" not in st.session_state:
        st.session_state.messages_webexplorer_1 = [initial_assistant_message]
    