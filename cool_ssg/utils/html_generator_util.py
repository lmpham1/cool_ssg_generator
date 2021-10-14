import shutil
import re
from pathlib import Path

# Generate HTML file from filepath, and export to output folder
def generateFromFile(filepath, output, options):
    # extract file name without extension
    filename = Path(filepath).stem

    with open(filepath, encoding='utf8') as (file):
        contents = ''.join(file.readlines())
        outputFilePath = Path(output).joinpath(filename + ".html")

        outContent = createHTMLString(filename, contents, outputFilePath, options)
        
        if(filepath.name.endswith(".md")):
            outContent = processMarkdown(outContent)
    
        output.mkdir(parents=True, exist_ok=True)

        outputFile = open(outputFilePath, "w", encoding="utf-8")
        outputFile.write(outContent)
        outputFile.close()
        print("\"" + filename + ".html\" generated successfully!")
        

# Generate HTML files with the same structure as the input folder, and export to output folder
def generateFromDirectory(inDir, output, options):
    links = []
    for filepath in Path(inDir).rglob("*.*"):
        title = Path(filepath).stem
        outputPath = Path(output).joinpath(Path(filepath).parents[0].relative_to(inDir))
        generateFromFile(filepath, outputPath, options)
        links.append("<a class=\"list-item\" href=\"{file}\"><li class=\"link\">{title}</li></a>".format(file=outputPath.joinpath(title + ".html").relative_to(output), title=title))
    
    indexSkeleton = """<!doctype html>
<html lang="{lang}">
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
        {stylesheets}
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>{title}</h1>
        <ul class=\"link-container\">
            {contents}
        </ul>
    </body>
</html>"""

    styleHTML = ""
    if options["stylesheets"] is not None:
        for stylesheet in options["stylesheets"]:
            styleHTML += "<link rel=\"stylesheet\" href=\"{}\">\n".format(stylesheet)
    
    indexTitle = Path(inDir).name

    indexHTMLContents = indexSkeleton.format(stylesheets=styleHTML, contents='\n'.join(links), title=indexTitle if indexTitle != '' and indexTitle is not None else "Index Page", lang=options["lang"])

    outputFile = open(Path(output).joinpath("index.html"), "w", encoding="utf-8")
    outputFile.write(indexHTMLContents)
    outputFile.close()

# Create HTML from markdown file
def processMarkdown(htmlContent):
    
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
def createHTMLString(filename, contents, output, options):
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
        {stylesheets}
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>{title}</h1>
        {contents}
    </body>
</html>"""

    styleHTML = ""
    if options["stylesheets"] is not None:
        for stylesheet in options["stylesheets"]:
            if isinstance(stylesheet, Path):
                for part in range(0, len(output.parts) - 2):
                    stylesheet = Path("..").joinpath(stylesheet)
            styleHTML += "<link rel=\"stylesheet\" href=\"{}\">\n".format(stylesheet)
    
    return htmlSkeleton.format(title=title, contents=contents, stylesheets=styleHTML, lang=options["lang"])

# emptying old output folder
def emptyFolder(dir):
    shutil.rmtree(dir)
    Path(dir).mkdir()

# generate stylesheet files in <OUTPUT>/public/stylesheet/
def generate_stylesheets(stylesheets, output):
    stylesheet_paths = []

    # default stylesheet
    default_stylesheet = "public/stylesheet/default.css"
    stylesheet_folder = Path(output).joinpath('public', 'stylesheet')
    Path(stylesheet_folder).mkdir(parents=True, exist_ok=True)

    if stylesheets:        
        for stylesheet in stylesheets:
            if stylesheet.startswith("https://") or stylesheet.startswith("http://"):
                stylesheet_paths.append(stylesheet)
            elif Path(stylesheet).is_file() and Path(stylesheet).exists():
                shutil.copy(stylesheet, stylesheet_folder)
                stylesheet_paths.append(stylesheet_folder.joinpath(Path(stylesheet).name).relative_to(output))
            else:
                print("ERROR: Cannot find stylesheet: {}".format(stylesheet))
    else:
        shutil.copy(default_stylesheet, stylesheet_folder)
        stylesheet_paths.append(stylesheet_folder.joinpath(Path(default_stylesheet).name).relative_to(output))
    
    return stylesheet_paths
