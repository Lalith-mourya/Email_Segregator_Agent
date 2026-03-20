import streamlit as st
from agent import SpamModelBasedAgent

# Load agent
agent = SpamModelBasedAgent("models/spam_model.pkl")

# Page title
st.title("📧 Spam Detection Agent")
st.write("Hybrid AI Agent (Rule-Based + ML Model)")

# User input
subject = st.text_input("Enter Email Subject")

# Predict button
if st.button("Predict"):
    if subject.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction, source = agent.predict(subject)

        if prediction == 1:
            st.error(f"🚨 SPAM (via {source})")
        else:
            st.success(f"✅ HAM (via {source})")
