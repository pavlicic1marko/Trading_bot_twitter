import openai
from dotenv import load_dotenv
import os

load_dotenv()


print("starting")

openai.api_key = os.getenv("CHAT_GPT_KEY")

# model options
gpt_4 = "gpt-4"
gpt_3x5_turbo = "gpt-3.5-turbo"

model_id = gpt_4
# Initial message to ask the first question
messages = [{"role": "user", "content": "is Serbia in the EU"}]

# Call the API
completion = openai.chat.completions.create(model=model_id, messages=messages)

# Print the answer we received for the 1st question
print(completion.choices[0].message.content)