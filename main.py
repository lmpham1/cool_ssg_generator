import argparse
import os
import sys
import helper

def main():
    args = parseArguments()
    input = args.input

    if input is None:
        print("ERROR: Input cannot be empty. Please specify input file or folder with --input flag, or refer to --help for documentation")
        sys.exit(1)

    stylesheets = args.stylesheet
    
    #check if output is specified
    if args.output is None:
        output = os.path.join('.', 'dist')
        helper.emptyFolder()
    elif os.path.exists(args.output[0]):
        output = args.output[0]
    else:
        print("ERROR: Could not find output folder")
        sys.exit(1)

    #check if input is a file or a directory
    for item in input:
        if os.path.isdir(item):
            helper.generateFromDirectory(item, output, stylesheets)
        elif os.path.isfile(item):
            helper.generateFromFile(item, output, stylesheets)
        else:
            print("ERROR: Could not find input file/folder")
    

def parseArguments():
    parser = argparse.ArgumentParser(description="Generate HTML website from raw data")
    #master_group = parser.add_mutually_exclusive_group()
    #version_group = master_group.add_argument_group("Version", "flag to show program's version")
    #other_group = master_group.add_argument_group("Others", "other flags and arguments")
    parser.add_argument('-v', '--version', action='version', version='cool_ssg_generator release 0.1', help='display the current version')
    parser.add_argument('-i', '--input', nargs='+', help='path to input file or directory', required=True)
    parser.add_argument('-o', '--output', nargs=1, help='path to output directory')
    parser.add_argument('-s', '--stylesheet', nargs='+', help='attach stylesheet URL')
    args = parser.parse_args()
    return args

main()