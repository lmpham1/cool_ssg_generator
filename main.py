import argparse
import os
import helper

def main():
    args = parseArguments()
    input = args.input
    stylesheets = args.stylesheet
    
    if args.output is None:
        output = ".\dist"
        helper.emptyFolder()
    elif os.path.exists(args.output[0]):
        output = args.output[0]
    else:
        print("ERROR: Could not find output folder")
        quit()

    #check if input is a file or a directory
    for item in input:
        #item = item.replace("/", "\\")
        if os.path.isdir(item):
            helper.generateFromDirectory(item, output, stylesheets)
        elif os.path.isfile(item):
            helper.generateFromFile(item, output, stylesheets)
        else:
            print("ERROR: Could not find input file/folder")
    

def parseArguments():
    parser = argparse.ArgumentParser(description="Generate HTML website from raw data")
    parser.add_argument('-v', '--version', dest='version', action='version', version='cool_ssg_generator release 0.1', help='display the current version')
    parser.add_argument('-i', '--input', nargs='*', help='path to input file or directory')
    parser.add_argument('-o', '--output', nargs=1, help='path to output directory')
    parser.add_argument('-s', '--stylesheet', nargs='*', help='attach stylesheet URL')
    args = parser.parse_args()
    return args

main()