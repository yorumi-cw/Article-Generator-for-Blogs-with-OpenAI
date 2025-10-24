
import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

client = openai.OpenAI(api_key=api_key)

def generate_blog(paragraph_topic):
    response = client.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt=f"Write a paragraph about the following topic: {paragraph_topic}",
        max_tokens=400,
        temperature=0.5
    )
    return response.choices[0].text.strip()

keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? Y for yes, anything else for no: ")
    if answer.strip().lower() == 'y':
        topic = input("What should this paragraph talk about? ")
        print("\n📝 Generated Paragraph:\n")
        print(generate_blog(topic))
        print("\n" + "-"*50 + "\n")
    else:
        keep_writing = False
