import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def getgpt(userinput):
    response = openai.Completion.create(
        engine="davinci",
        prompt=userinput.strip(),
        temperature=0.8, # One of the most important settings to control the output of the GPT-3 engine is the temperature. This setting controls the randomness of the generated text. A value of 0 makes the engine deterministic, which means that it will always generate the same output for a given input text.
        max_tokens=1000, 
        top_p=1.0,
        frequency_penalty=0.0, # Frequency penalty works by lowering the chances of a word being selected again the more times that word has already been used. Frequency Penalty is a way to prevent word repetitions
        presence_penalty=0.0, # Presence penalty does not consider how frequently a word has been used, but just if the word exists in the text. Presence Penalty is a way to prevent topic repetitions.
        stop=["\n"]
    )

    return response["choices"][0]["text"]

def rewrite_temp_gpt3_without_pandoc(input_user_prompt, input_title):
    # read in html gpt3 page to include new content
    with open('templates/templates/2021/07/11/temp_gpt3.html') as f:
        html_lines = f.readlines()

    # remove last 8 lines
    html_lines.pop()
    html_lines.pop()
    html_lines.pop()
    html_lines.pop()
    html_lines.pop()
    html_lines.pop()
    html_lines.pop()

    article_body = getgpt(input_user_prompt)

    html_lines.append('<br>\n')
    html_lines.append('<h1 style="margin-bottom:7px">'+str(input_title.strip())+'</h1>\n')
    html_lines.append('<small style="float:left; color: #888"> 2021 Jul 11 </small>\n')
    html_lines.append('<small style="float:right; color: #888"><a href="/">See all posts</a></small>\n')
    html_lines.append('<br> <br> <br>\n')
    html_lines.append('<p>'+str(input_user_prompt.strip()) + str(article_body.strip())+'</p>\n')
    html_lines.append('</div>')

    # re-write the new app code
    html_out = open("templates/templates/2021/07/11/temp_gpt3.html", "w")
    for line in html_lines:
        html_out.write(line)