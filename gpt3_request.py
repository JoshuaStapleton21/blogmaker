import os
import openai
from dotenv import load_dotenv
import json
from test_gpt3 import getgpt
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_open_api_response(user_prompt, title):
    # print(user_prompt)
    print(user_prompt.strip())
    response = getgpt(user_prompt.strip())
    
    # print(len(response))
    # while len(response) < 1000:
    #     print("Response is less than 1000 characters, increasing response length")
    #     response.append(getgpt(user_prompt.strip()))

    hoi = []
    hoi.append("[category]: <> (Philosophy)\n")
    hoi.append("[date]: <> (2021/07/11)\n")
    hoi.append("[title]: <> (" + title.strip() + ")")
    hoi.append("\n")

    # append the user prompt
    for line in user_prompt:
        hoi.append(line)

    # get the response and append
    hoi.append(response)
    
    # create an md page.
    app_out = open("posts/temp_gpt3.md", "w")
    for line in hoi:
        app_out.write(line)

    
