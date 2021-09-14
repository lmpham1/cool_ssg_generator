import os
import shutil

def generateFromFile(inFile, output, stylesheets):
    filename = inFile[inFile.replace("\\","/").rfind("/")+1:inFile.rfind(".")]
    #print(filename)
    #print(output + "/" + filename + ".html")
    with open(inFile, encoding='utf8') as (file):
        contents = file.readlines()
        outContent = createHTMLString(filename, contents, stylesheets)
        if not os.path.exists(output):
            os.mkdir(output)
        outputFile = open(output + "/" + filename + ".html", "w", encoding="utf-8")
        outputFile.write(outContent)
        outputFile.close()
        print("\"" + filename + ".html\" generated successfully!")

def generateFromDirectory(inDir, output, stylesheets):
    for root, dirs, files in os.walk(inDir):
        for file in files:
            filepath = os.path.join(root, file)
            outputPath = filepath[filepath.find('\\'):filepath.rfind('\\')].replace("\\","/")
            generateFromFile(filepath, output + outputPath, stylesheets)

def createHTMLString(filename, contents, stylesheets):

    index = 0

    title = filename

    while index < len(contents):
        contents[index] = contents[index].strip()
        if index == 0 and len(contents[index]) != 0 and len(contents[index+1].strip()) == 0 and len(contents[index+2].strip()) == 0:
            title = contents[0]
            contents[0] = "<h1>" + contents[0] + "</h1>"
            index = 3
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