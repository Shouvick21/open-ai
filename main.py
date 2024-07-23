from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a proficient email writer,who is skilled at writing profetional email based on user input"},
    {"role": "user", "content": "write an email for regisnation"}
  ]
)

print(completion.choices[0].message)
# import openai
# print(openai.__version__)
