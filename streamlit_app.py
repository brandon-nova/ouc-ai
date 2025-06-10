import streamlit as st
from groq import Groq

# --- Configuration ---
API_KEY = "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"
client = Groq(api_key=API_KEY)
MODEL = "gemma2-9b-it"

# --- Streamlit UI ---
st.set_page_config(page_title="search.ouc.com", page_icon="💡", layout="wide")

# Force light theme via CSS variables override
st.markdown(
    """
    <style>
    /* 1) Full-app white */
    body, [data-testid="stAppViewContainer"], .block-container {
      background: #fff !important;
    }

    /* 2) Center the logo */
    [data-testid="stImage"] > figure {
      display: block !important;
      margin-left: auto;
      margin-right: auto;
      text-align: center;

    }

    /* 3) Headline blue & centered */
    .block-container h1 {
      color: #1a68ba !important;
      text-align: center;
    }

    /* 4) Chat area white */
    [data-testid="stChatMessageList"] {
      background: #fff !important;
    }

    /* 5) All chat text in #1a68ba */
    [data-testid="stChatMessage"] div[data-testid="stMarkdownContainer"] {
      color: #1a68ba !important;
    }

    /* 6) (Optional) Input box blue */
    [data-testid="stChatInput"] textarea {
      background: #1a68ba !important;
      color: #fff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



# Display a logo/image above the title (place 'logo.png' in your app folder or use a URL)
st.image("logo.png", use_container_width=False, width=200)
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
