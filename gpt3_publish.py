# publish to html
import os

def publish_gtp3_output():
    os.system('./publish.py posts/' + str('temp_gpt3') + '.md')