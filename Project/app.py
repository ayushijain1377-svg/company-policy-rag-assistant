import streamlit as st

from src.agent import agent


# =====================================================
# 1. PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Venus Company Policy AI",
    page_icon="🏢"
)


# =====================================================
# 2. TITLE
# =====================================================

st.title("🏢 Venus Company Policy AI")

st.write(
    "Ask questions about the Venus company policy."
)


# =====================================================
# 3. CHAT HISTORY
# =====================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# =====================================================
# 4. DISPLAY PREVIOUS MESSAGES
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# =====================================================
# 5. USER QUESTION
# =====================================================

question = st.chat_input(
    "Ask a question about company policy..."
)


# =====================================================
# 6. PROCESS QUESTION
# =====================================================

if question:

    # -------------------------------------------------
    # Display user question
    # -------------------------------------------------

    with st.chat_message("user"):

        st.write(question)


    # -------------------------------------------------
    # Save user question
    # -------------------------------------------------

    st.session_state.messages.append({

        "role": "user",

        "content": question

    })


    # =================================================
    # 7. CREATE CHAT HISTORY
    # =================================================

    chat_history = ""

    for message in st.session_state.messages:

        chat_history += (
            f'{message["role"]}: '
            f'{message["content"]}\n'
        )


    # =================================================
    # 8. RUN RAG AGENT
    # =================================================

    with st.chat_message("assistant"):

        with st.spinner(
            "🔎 Searching company policy..."
        ):

            result = agent.invoke({

                "question": question,

                "context": "",

                "answer": "",

                "chat_history": chat_history

            })


        # =================================================
        # 9. GET ANSWER
        # =================================================

        answer = result["answer"]


        # =================================================
        # 10. DISPLAY ANSWER
        # =================================================

        st.write(answer)


    # =================================================
    # 11. SAVE ANSWER
    # =================================================

    st.session_state.messages.append({

        "role": "assistant",

        "content": answer

    }) 