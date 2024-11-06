import os
from langchain_groq import ChatGroq

api_key = os.getenv("API_KEY")

llm = ChatGroq(
    api_key=api_key,
    model="llama3-8b-8192"
    )

context = "they are advanced types of artificial intelligence (AI) models designed to understand, generate, and manipulate human language. They are trained on massive datasets containing diverse language inputs to learn patterns, context, and nuances in language. LLMs are built using deep learning techniques, particularly neural networks."
prompt = f"""You are a knowledgeable educator with expertise in creating effective study materials and questions tailored to various subjects and topics. Your goal is to help students enhance their understanding and retention of information by generating insightful and thought-provoking questions based on provided materials. 

Your task is to generate study questions from the following material: {context}.

Keep in mind the key aspects of effective question formulation, such as ensuring a mix of question types (e.g., multiple-choice, short answer, essay) and aligning them with the main themes and concepts of the material. Additionally, aim to create questions that promote critical thinking and encourage deeper engagement with the content. 

Please ensure the questions are clear, concise, and appropriate for the intended audience."""
q = llm.invoke(prompt)
print(q.content)