import streamlit as st
from groq import Groq

# --- Configuration ---
API_KEY = "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"
client = Groq(api_key=API_KEY)
MODEL = "gemma2-9b-it"

# --- Streamlit UI ---
st.set_page_config(page_title="search.ouc.com", page_icon="💡", layout="wide")

# Force light theme via CSS variables override
def apply_light_theme():
    st.markdown(
        """
        <style>
        :root {
            --primary-background-color: #FFFFFF !important;
            --secondary-background-color: #FFFFFF !important;
            --tertiary-background-color: #FFFFFF !important;
            --text-color: #000000 !important;
        }
        #MainMenu, header, footer {
            visibility: hidden;
            height: 0;
            margin: 0;
            padding: 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

apply_light_theme()
st.title("search.ouc.com")

# Initialize chat history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
prompt = st.chat_input("Type your message...")

# When user sends a message
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    # Call Groq chat API
    response = client.chat.completions.create(
        model=MODEL,
        messages=st.session_state.history
    )
    reply = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": reply})

# Display chat history
for msg in st.session_state.history:
    st.chat_message(msg["role"]).write(msg["content"])
