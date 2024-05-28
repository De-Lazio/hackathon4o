import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Charger le tokenizer et le modèle LLaMA 3
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B")

def generate_questions(course_content, num_questions=5):
    prompt = f"Générer {num_questions} questions d'évaluation basées sur le contenu suivant:\n\n{course_content}\n\nQuestions:"
    inputs = tokenizer(prompt, return_tensors="pt")

    # Générer des questions
    output = model.generate(inputs.input_ids, max_length=500, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extraire les questions générées
    questions = generated_text.split('\n')[1:num_questions+1]
    return questions

# Interface utilisateur Streamlit
st.title("Générateur de Questions d'Évaluation")

st.write("Entrez le contenu du cours ci-dessous :")
course_content = st.text_area("Contenu du cours", height=300)

num_questions = st.slider("Nombre de questions à générer", 1, 10, 5)

if st.button("Générer des Questions"):
    with st.spinner("Génération des questions..."):
        questions = generate_questions(course_content, num_questions=num_questions)
        st.success("Questions générées avec succès !")
        for i, question in enumerate(questions, 1):
            st.write(f"Question {i}: {question}")

