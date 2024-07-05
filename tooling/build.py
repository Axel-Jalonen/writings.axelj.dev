import os
import sys

def read_and_write_post(fileName):
    with open(fileName, "r") as file: 
        content = file.read()
        lines = content.splitlines()
        title = lines[0]
        personal_site = lines[2]
        author = lines[4]
        intro = lines[6]
        first_paragraph = lines[8]
        paragraphs = []
        for line in lines[10:]:
            if not line == "\n":
                paragraphs.append(line)
        with open("template.html", "r") as file:
            content = file.read()
            content = content.replace("${TITLE}", title)
            content = content.replace("${SITE}", personal_site)
            content = content.replace("${AUTHOR}", author)
            content = content.replace("${INTRO}", intro)
            content = content.replace("${FIRST_PARAGRAPH}", first_paragraph)
            markup = ""
            for paragraph in paragraphs:
                markup += "<p>" + paragraph + "</p>"
            content = content.replace("${REST}", markup)
            fileName = "../build/pages/" + title.replace(" ", "-") + ".html"
            with open(fileName, "w") as file:
                file.write(content)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python buildPost.py <filename>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    read_and_write_post(input_file)
