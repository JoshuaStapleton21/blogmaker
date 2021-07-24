import os
from publish import publish_an_article
# essentially just updates the html page itself. No changes to app.py or index.html

########### THIS IS THE ONLY PARAMETER WHICH NEEDS TO BE CONFIGURED IN THE WHOLE FILE ##########
article_name = "ai_horror"
################################################################################################

args_in = ['/Users/joshuastapleton/Desktop/joshua_stapleton_blog/blogmaker/publish.py', 'posts/'+ str(article_name) + '.md']
publish_an_article(args_in)

# os.system('./publish.py posts/' + str(article_name) + '.md')