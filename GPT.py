from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv('.env')

client = OpenAI(api_key=os.getenv('api_key'))


class GPT_response:
    def __init__(self, user_text, user_prompt):
        self.user_text = user_text
        self.user_prompt = user_prompt

    def prompt_response(self):
        response = client.chat.completions.create(
          model="gpt-3.5-turbo-0125",
          messages=[
            {
              "role": "system",
              "content": f"{self.user_prompt}"
            },
            {
              "role": "user",
              "content": f"{self.user_text}"
            }
          ],
          temperature=1,
          max_tokens=2000,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )

        output = response.choices[0].message.content
        return output

