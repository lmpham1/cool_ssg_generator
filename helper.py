import os
import shutil
import re

# Generate HTML file from inFile, and export to output folder
def generateFromFile(inFile, output, stylesheets, lang):
    filename = re.search('(?!(\\|\/))[^\/\\\.]*(?=\.[A-Za-z0-9]+$)', inFile)[0]
    
    with open(inFile, encoding='utf8') as (file):
        contents = ''.join(file.readlines())
        
        if(inFile.endswith(".txt")):
            outContent = createHTMLString(filename, contents, stylesheets, lang)
        elif(inFile.endswith(".md")):
            outContent = createMarkdownString(filename, contents, stylesheets, lang)
    
        if not os.path.exists(output):
            os.makedirs(output)
        
        outputFile = open(os.path.join(output, filename + ".html"), "w", encoding="utf-8")
        outputFile.write(outContent)
        outputFile.close()
        print("\"" + filename + ".html\" generated successfully!")
        

# Generate HTML files with the same structure as the input folder, and export to output folder
def generateFromDirectory(inDir, output, stylesheets, lang):
    links = []
    for root, dirs, files in os.walk(inDir):
        for file in files:
            filepath = os.path.join(root, file)
            getFileSubfolder = re.search(r'(?<=\\|\/)(.*)(?=\\|\/[^\\\/]+)', filepath)
            outputPath = "" if getFileSubfolder is None else getFileSubfolder.group(1)
            
            generateFromFile(filepath, os.path.join(output, outputPath), stylesheets, lang)
            links.append("<a class=\"link\" href=\"{file}\">{title}</a>".format(file=os.path.join(".", outputPath, file[0:file.rfind('.')] + ".html"), title=file[0:file.rfind('.')]))
    
    indexSkeleton = """<!doctype html>
<html lang="{lang}">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
        <link rel="stylesheet" href="public/stylesheet/default.css">
        {stylesheets}
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>{title}</h1>
        <div class=\"link-container\">
            {contents}
        </div>
    </body>
</html>"""

    styleHTML = ""
    if stylesheets is not None:
        for stylesheet in stylesheets:
            styleHTML += "<link rel=\"stylesheet\" href=\"{}\">\n".format(stylesheet)
    
    indexTitle = inDir.split('\\')[-1] if inDir.split('\\')[-1] != '' else inDir.split('\\')[-2]

    indexHTMLContents = indexSkeleton.format(stylesheets=styleHTML, contents='\n'.join(links), title=indexTitle if indexTitle != '' and indexTitle is not None else "Index Page", lang=lang)

    outputFile = open(output + "/index.html", "w", encoding="utf-8")
    outputFile.write(indexHTMLContents)
    outputFile.close()

# Create HTML from markdown file
def createMarkdownString(filename, contents, stylesheets, lang):
    # Create title, paragraphs, and stylesheet first, like normal
    htmlContent = createHTMLString(filename, contents, stylesheets, lang)
    
    # Parse markdown
    htmlContent = re.sub('\*\*([^\s\*.]{1}.*?)\*\*|__([^\s_.]{1}.*?)__', r'<strong>\1\2</strong>', htmlContent)
    htmlContent = re.sub('\*([^\s\*.]{1}.*?)\*|_([^\s\_.]{1}.*?)_', r'<em>\1\2</em>', htmlContent)
    htmlContent = re.sub('\[(.+)\]\((.+)\)', r'<a href="\2">\1</a>', htmlContent)
    htmlContent = re.sub('(\n|(\n<p>))\s{0,3}((---)|(\*\*\*))\s{0,3}((</p>\n)|\n)', r'\n<hr/>\n', htmlContent)
    # blockQuoteParser = lambda matchedContent: "<blockquote>\n{}\n</blockquote>".format(re.sub("<\/?p>", "", matchedContent.group(1)))
    # htmlContent = re.sub(r'```\r?\n(((?!```)[\s\S])+)```', blockQuoteParser, htmlContent)

    return htmlContent

# Create HTML mark up and append the content
# return the complete HTML mark up for a page
def createHTMLString(filename, contents, stylesheets, lang):
    index = 0
    title = filename

    if contents.split('\n\n\n', 1)[0] == contents.splitlines()[0]:
        title = contents.split('\n\n\n', 1)[0]
        contents = contents.split('\n\n\n', 1)[1]

    contents = "<p>" + contents + "</p>"
    contents = contents.replace("\n\n", "</p>\n\n<p>")

    htmlSkeleton= """<!doctype html>
<html lang="{lang}">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
        <link rel="stylesheet" href="public/stylesheet/default.css">
        {stylesheets}
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>{title}</h1>
        {contents}
    </body>
</html>"""

    styleHTML = ""
    if stylesheets is not None:
        for stylesheet in stylesheets:
            styleHTML += "<link rel=\"stylesheet\" href=\"{}\">\n".format(stylesheet) 

    return htmlSkeleton.format(title=title, contents=contents, stylesheets=styleHTML, lang=lang)

# emptying old output folder
def emptyFolder():
    shutil.rmtree('./dist')
    os.mkdir('./dist')
