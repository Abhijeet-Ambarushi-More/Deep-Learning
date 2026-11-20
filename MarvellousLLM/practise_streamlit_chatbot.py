
import streamlit as st
from ollama import Client

client = Client(host="http://127.0.0.1:11434")

# Page configuration
st.set_page_config(
    page_title="Marvellous Python Tutor"
)

# Application title
st.title("Marvellous Python Tutor")
st.caption("AI programming teacher by using streamlit and Ollama")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a Python programming teacher. "
                       "Explain concepts clearly with examples."
        }
    ]

# Display previous conversation
for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
question = st.chat_input("Ask me anything about Python...")

if question:
    # Save user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Marvellous AI is thinking..."):
            try:
                response = client.chat(
                    model="llama3.2:1b",
                    messages=st.session_state.messages
                )

                answer = response.message.content
                st.markdown(answer)

                # Save assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as error:
                st.error(f"Something went wrong: {error}")
