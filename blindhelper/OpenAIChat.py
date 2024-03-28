import openai
import os

class OpenAIChat:
    def __init__(self):
        self.openai_api_key = os.environ.get('OPENAI_API_KEY')
        self.model = "gpt-4"

    def get_completion(self, prompt, temperature=0):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message["content"]




  