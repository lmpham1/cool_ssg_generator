import argparse
import os
import sys
import helper
import json


def main():
    args = parseArguments()

    config = args.config[0] if args.config else None

    # if config file exists, overwrite all args
    if config:
        if os.path.exists(config):
            loadedConfig = json.load(open(config, "r"))
            if "input" in loadedConfig:
                args.input = [loadedConfig["input"]]
            else:
                print(
                    "ERROR: Input cannot be empty. Please specify input file or folder in the configuration.")
                sys.exit(1)
            if "stylesheet" in loadedConfig:
                args.stylesheet = [loadedConfig["stylesheet"]]
            if "lang" in loadedConfig:
                args.lang = [loadedConfig["lang"]]
            if "output" in loadedConfig:
                args.output = [loadedConfig["output"]]
        else:
            print("ERROR: Could not find config file")
            sys.exit(1)
    input = args.input

    if input is None:
        print("ERROR: Input cannot be empty. Please specify input file or folder with --input flag, or refer to --help for documentation")
        sys.exit(1)

    stylesheets = args.stylesheet
    lang = 'en-CA' if args.lang is None else args.lang[0]

    # check if output is specified
    if args.output is None:
        output = os.path.join('.', 'dist')
        helper.emptyFolder()
    elif os.path.exists(args.output[0]):
        output = args.output[0]
    else:
        print("ERROR: Could not find output folder")
        sys.exit(1)
    # check if input is a file or a directory
    for item in input:
        if os.path.isdir(item):
            helper.generateFromDirectory(item, output, stylesheets, lang)
        elif os.path.isfile(item):
            # print(item, output, stylesheets, lang)
            helper.generateFromFile(item, output, stylesheets, lang)
        else:
            print("ERROR: Could not find input file/folder")


def parseArguments():
    parser = argparse.ArgumentParser(
        description="Generate HTML website from raw data")
    #master_group = parser.add_mutually_exclusive_group()
    #version_group = master_group.add_argument_group("Version", "flag to show program's version")
    #other_group = master_group.add_argument_group("Others", "other flags and arguments")
    parser.add_argument('-v', '--version', action='version',
                        version='cool_ssg_generator release 0.1', help='display the current version')
    parser.add_argument('-i', '--input', nargs='+',
                        help='path to input file or directory')
    parser.add_argument('-o', '--output', nargs=1,
                        help='path to output directory')
    parser.add_argument('-s', '--stylesheet', nargs='+',
                        help='attach stylesheet URL')
    parser.add_argument('-l', '--lang', nargs=1,
                        help='language of the generated documents, default is en-CA')
    parser.add_argument('-c', '--config', nargs=1,
                        help='path to the config file')

    args = parser.parse_args()
    return args


main()
