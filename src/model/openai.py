from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_TOKEN")


def gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    prompt_response = response["choices"][0]["message"]["content"]
    tokens_used = response["usage"]["prompt_tokens"]

    return prompt_response, tokens_used
