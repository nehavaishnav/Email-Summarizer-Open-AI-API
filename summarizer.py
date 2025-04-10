import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_email(content):
    try:
        prompt = f"Summarize the following email content in simple points:\n\n{content}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.5
        )
        summary = response['choices'][0]['message']['content']
        return summary.strip()
    except Exception as e:
        return f"Error during summarization: {e}"
