import streamlit as st

from src.classifier import classify_persona
from src.rag_pipeline import RAGPipeline
from src.generator import generate_response
from src.escalator import should_escalate


st.set_page_config(
    page_title="Persona Support Agent",
    page_icon="🤖",
    layout="wide"
)

# -------------------
# Sidebar
# -------------------

st.sidebar.title("🤖 Persona Support Agent")

st.sidebar.markdown("""
### Features

✅ Persona Classification

✅ RAG Retrieval

✅ Gemini Response Generation

✅ Human Escalation

✅ Confidence Scoring

✅ Feedback Collection
""")

# -------------------
# Main UI
# -------------------

st.title("🤖 Persona-Aware Customer Support Agent")

st.write(
    "Ask a support question and receive a persona-aware AI response."
)

question = st.text_area(
    "Enter your question:"
)

if st.button("Submit"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        # Escalation check

        if should_escalate(question):

            st.error(
                "⚠ Escalation Required. Please connect with Human Support."
            )

        else:

            # Persona Classification

            persona_result = classify_persona(question)

            persona = persona_result["persona"]

            confidence = persona_result["confidence"]

            # RAG

            rag = RAGPipeline()

            rag.create_vectorstore()

            context = rag.retrieve_context(question)

            # Generate Response

            response = generate_response(
                question=question,
                context=context,
                persona=persona
            )

            # Display Results

            st.subheader("Detected Persona")

            st.success(persona)

            st.subheader("Confidence Score")

            st.progress(float(confidence))

            st.write(
                f"{confidence*100:.0f}% confidence"
            )

            st.subheader("AI Response")

            st.write(response)

            # Feedback

            st.subheader("Feedback")

            feedback = st.radio(
                "Was this response helpful?",
                ["👍 Yes", "👎 No"]
            )

            if st.button("Submit Feedback"):

                st.success(
                    "Thank you for your feedback!"
                )