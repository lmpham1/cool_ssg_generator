import sys
from pathlib import Path

from utils import html_generator_util
from utils import arguments_util


def main():
    options = arguments_util.parse_arguments()

    input = options["input"]
    output = options["output"]

    if input is None:
        print(
            "ERROR: Input cannot be empty. Please specify input file or folder with --input flag, or refer to --help for documentation"
        )
        sys.exit(1)

    # check if output is specified
    if output is None:
        output = Path(".").joinpath("dist")
    elif not Path(output).exists():
        print("ERROR: Could not find output folder")
        sys.exit(1)

    html_generator_util.empty_folder(output)
    options["stylesheets"] = html_generator_util.generate_stylesheets(
        options["stylesheets"], output
    )

    # check if input is a file or a directory
    for item in input:
        if Path(item).is_dir():
            html_generator_util.generate_from_directory(item, output, options)
        elif Path(item).is_file():
            # print(item, output, stylesheets, lang)
            html_generator_util.generate_from_file(item, output, options)
        else:
            print("ERROR: Could not find input file/folder")


if __name__ == "__main__":
    main()
