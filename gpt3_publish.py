# publish to html
import os

def publish_gtp3_output():
    path = os.getcwd()
    os.system(str(path) + '/publish.py posts/' + str('temp_gpt3') + '.md')