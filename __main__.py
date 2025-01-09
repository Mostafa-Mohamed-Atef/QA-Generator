import streamlit as st
from langchain_groq import ChatGroq

# Load API key from environment variables
def getting_api_key():
    with open("API_KEY.txt", 'r') as file:
        return file.readline().strip()

api_key = getting_api_key()

# Initialize the LLM model
llm = ChatGroq(
    api_key=api_key,
    model="llama3-8b-8192"
)

# Streamlit app
st.title("Study Question Generator")
st.write("Generate insightful and thought-provoking study questions from your notes.")

# Input for notes/context
context = st.text_area("Enter your notes:", placeholder="Type or paste your study material here...")

# Button to trigger the LLM
if st.button("Generate Questions"):
    if context.strip():  # Check if input is not empty
        prompt = f"""You are a knowledgeable educator with expertise in creating effective study materials and questions tailored to various subjects and topics. Your goal is to help students enhance their understanding and retention of information by generating insightful and thought-provoking questions based on provided materials. 

        Your task is to generate study questions from the following material: {context}.

        Keep in mind the key aspects of effective question formulation, such as ensuring a mix of question types (e.g., multiple-choice, short answer, essay) and aligning them with the main themes and concepts of the material. Additionally, aim to create questions that promote critical thinking and encourage deeper engagement with the content. 

        Please ensure the questions are clear, concise, and appropriate for the intended audience."""
        
        try:
            # Invoke the model
            response = llm.invoke(prompt)
            # Display output
            st.subheader("Generated Study Questions")
            st.write(response.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some notes to generate questions!")
