import openai
from api_secrets import API_KEY_OPENAI

openai.api_key = API_KEY_OPENAI


def ask_computer(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100)

    return response["choices"][0]["text"]
