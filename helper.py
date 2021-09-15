import os
import shutil

# Generate HTML file from inFile, and export to output folder
def generateFromFile(inFile, output, stylesheets):
    filename = inFile[inFile.replace("\\","/").rfind("/")+1:inFile.rfind(".")]

    with open(inFile, encoding='utf8') as (file):
        contents = file.readlines()
        outContent = createHTMLString(filename, contents, stylesheets)

        if not os.path.exists(output):
            os.mkdir(output)
        
        outputFile = open(output + "/" + filename + ".html", "w", encoding="utf-8")
        outputFile.write(outContent)
        outputFile.close()
        print("\"" + filename + ".html\" generated successfully!")

# Generate HTML files with the same structure as the input folder, and export to output folder
def generateFromDirectory(inDir, output, stylesheets):
    for root, dirs, files in os.walk(inDir):
        for file in files:
            filepath = os.path.join(root, file)
            outputPath = filepath[filepath.find('\\'):filepath.rfind('\\')].replace("\\","/")
            generateFromFile(filepath, output + outputPath, stylesheets)

# Create HTML mark up and append the content
# return the complete HTML mark up for a page
def createHTMLString(filename, contents, stylesheets):
    index = 0
    title = filename

    while index < len(contents):
        contents[index] = contents[index].strip()
        if index == 0 and len(contents[index]) != 0 and len(contents[index+1].strip()) == 0 and len(contents[index+2].strip()) == 0:
            title = contents[0]
            contents[0] = "<h1>" + contents[0] + "</h1>\n<p>"
            index = 3
        elif index == 0:
            contents[index] = "<p>" + contents[index]
        if len(contents[index]) == 0:
            contents[index] = """</p>
                <p>
            """
        index+=1

    htmlSkeleton= """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>{title}</title>
                {stylesheets}
                <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <body>
            {contents}
            </body>
        </html>    
    """

    styleHTML = ""
    for stylesheet in stylesheets:
        if stylesheet is not None:
            styleHTML += "<link rel=\"stylesheet\" href={}>\n".format(stylesheet)
    
    transformedContent = ''.join(contents)    

    return htmlSkeleton.format(title=title, contents=transformedContent, stylesheets=styleHTML)

# emptying old output folder
def emptyFolder():
    output = './dist'
    if os.path.exists(output):
        for root, dirs, files in os.walk('./dist'):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
        os.rmdir('./dist')
    os.mkdir('./dist')