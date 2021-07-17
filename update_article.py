import os

# essentially just updates the html page itself. No changes to app.py or index.html

########### THIS IS THE ONLY PARAMETER WHICH NEEDS TO BE CONFIGURED IN THE WHOLE FILE ##########
article_name = "ai_horror"
################################################################################################

os.system('./publish.py posts/' + str(article_name) + '.md')