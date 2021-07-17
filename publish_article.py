import os

########### THIS IS THE ONLY PARAMETER WHICH NEEDS TO BE CONFIGURED IN THE WHOLE FILE ##########
article_name = "hoi"
################################################################################################


def extract_metadata(fil, filename=None):
    metadata = {}
    if filename:
        assert filename[-3:] == '.md'
        metadata["filename"] = filename[:-3]+'.html'
    while 1:
        line = fil.readline()
        if line and line[0] == '[' and ']' in line:
            key = line[1:line.find(']')]
            value_start = line.find('(')+1
            value_end = line.rfind(')')
            if key in ('category', 'categories'):
                metadata['categories'] = set([
                    x.strip().lower() for x in line[value_start:value_end].split(',')
                ])
                assert '' not in metadata['categories']
            else:
                metadata[key] = line[value_start:value_end]
        else:
            break
    return metadata


# read in metadata about the post
global_config = extract_metadata(open('config.md'))
file_location = "posts/"+str(article_name)+".md"
filename = os.path.split(file_location)[1]
metadata = extract_metadata(open(file_location), filename)
article_title = metadata['title']
date = metadata['date']


# first transform new post to html
os.system('./publish.py posts/' + str(article_name) + '.md')




# # second change the html page to include new post # #
with open('templates/index.html') as f:
    html_lines = f.readlines()

# remove the last ul tag
html_lines.pop()

html_lines.append('  <li>\n')
html_lines.append('    <span class="post-meta">'+ str(date) +'</span>\n')
html_lines.append('    <h3>\n')
html_lines.append('      <a class="post-link" href="'+ str(article_name)+'.html">'+ str(article_title)+'</a>\n')
html_lines.append('    </h3>\n')
html_lines.append('  </li>\n')

# re-write the new app code
html_out = open("templates/index.html", "w")
for line in html_lines:
     html_out.write(line)

# re-add the last line
html_out.write('</ul>')




# # third change the app file to include new post # #
with open('app.py') as f:
    app_lines = f.readlines()

app_lines.pop()
app_lines.pop()

# add ther new flask method to show the article
app_lines.append("@app.route('/"+ str(article_name) +".html')\n")
app_lines.append('def '+ str(article_name) + '():\n')
app_lines.append("    return render_template('templates/"+ str(date) +"/"+ str(article_name) + ".html')\n")

# re-write the new app code
app_out = open("app.py", "w")
for line in app_lines:
     app_out.write(line)

# re-add the last two lines
app_out.write("\n")
app_out.write("if __name__ == '__main__': # there is always one line between the last app route and these last two lines\n")
app_out.write("    app.run(debug=True)")