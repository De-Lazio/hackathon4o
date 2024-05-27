import openai


# Configuration de l'API
openai.api_key = "VOTRE_CLE_API"


#Function for generating the course which takes the theme
def generate_course(topic):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert educator."},
            {"role": "user", "content": f"Generate a comprehensive course on {topic}."}
        ]
    )
    course_content = response['choices'][0]['message']['content'].strip()
    return course_content

#Function for generating the cours questions which takes the theme
def generate_evaluation_questions(course_content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert educator."},
            {"role": "user", "content": f"Based on the following course content, generate 10 evaluation questions:\n\n{course_content}"}
        ]
    )
    questions = response['choices'][0]['message']['content'].strip()
    return questions

#Function for generating the question answers which takes the theme and user question
def answer_question(course_content, user_question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert educator."},
            {"role": "user", "content": f"Based on the following course content, answer the user's question:\n\nCourse content: {course_content}\n\nUser's question: {user_question}"}
        ]
    )
    answer = response['choices'][0]['message']['content'].strip()
    return answer



