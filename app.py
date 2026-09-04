import json
import streamlit as st
from services.gemini_service import analyze_customer_message

st.set_page_config(
    page_title="AI Customer Support",
    page_icon="🤖",
    layout="centered"
)

def load_test_messages():
    with open("data/test_messages.json", "r", encoding="utf-8") as file:
        return json.load(file)

st.title("🤖 AI Customer Support Assistant")

st.write(
    "Analyze customer messages using AI for "
    "category, sentiment, and automatic reply."
)

st.divider()

messages = load_test_messages()

selected_message = st.selectbox(
    "Choose a test message",
    ["Custom Message"] + [
        item["message"] for item in messages
    ]
)

if selected_message == "Custom Message":
    customer_message = st.text_area(
        "Customer Message",
        placeholder="Enter a customer message...",
        height=150
    )
else:
    customer_message = selected_message

if st.button("🤖 Analyze Message", use_container_width=True):

    if not customer_message.strip():
        st.warning("Please enter a customer message.")

    else:
        with st.spinner("AI is processing the message..."):
            try:
                result = analyze_customer_message(customer_message)

                st.success("Analysis completed!")

                st.subheader("💬 Customer Message")
                st.write(customer_message)

                st.subheader("📂 Category")
                st.info(result["category"])

                st.subheader("😊 Sentiment")

                if result["sentiment"] == "Positive":
                    st.success(result["sentiment"])
                elif result["sentiment"] == "Negative":
                    st.error(result["sentiment"])
                else:
                    st.info(result["sentiment"])

                st.subheader("🤖 Auto Reply")
                st.success(result["auto_reply"])

            except Exception as error:
                st.error(f"Error: {error}")