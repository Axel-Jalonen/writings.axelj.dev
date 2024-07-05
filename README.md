# My simple blog generator

## Why 

Because I wanted a convenient way to write blogs in plain text and have them come out looking good, without using complicated pipelines.

## How

Write your blog using this rigid template:

```plaintext
TITLE

PERSONAL SITE

NAME

INTRODUCTION PARAGRAPH

CONTENT PARAGRAPHS

...

```

Then run the build.py script from the tooling directory with your `txt` file as an argument to generate the HTML page which lives in the build folder.

e.g.:

`python3 ./build.py ../src/stop-using-install-scripts.txt`
