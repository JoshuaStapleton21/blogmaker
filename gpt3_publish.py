# publish to html
import os
from publish import publish_an_article

def publish_gtp3_output():
    args_in = ['/Users/joshuastapleton/Desktop/joshua_stapleton_blog/blogmaker/publish.py', 'posts/temp_gpt3.md']
    publish_an_article(args_in)