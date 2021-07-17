import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# https://www.twilio.com/blog/ultimate-guide-openai-gpt-3-language-model
response = openai.Completion.create(
  engine="davinci",
  prompt="Once there was a girl named",
  temperature=0.8, # One of the most important settings to control the output of the GPT-3 engine is the temperature. This setting controls the randomness of the generated text. A value of 0 makes the engine deterministic, which means that it will always generate the same output for a given input text.
  max_tokens=60, 
  top_p=1.0,
  frequency_penalty=0.0, # Frequency penalty works by lowering the chances of a word being selected again the more times that word has already been used. Frequency Penalty is a way to prevent word repetitions
  presence_penalty=0.0, # Presence penalty does not consider how frequently a word has been used, but just if the word exists in the text. Presence Penalty is a way to prevent topic repetitions.
  stop=["\n"]
)

hoi = response["choices"][0]["text"]
print(hoi)