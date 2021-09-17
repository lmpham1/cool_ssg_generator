# cool_ssg_generator
A simple SSG generator made with Python.
Current version is 0.1.0

### Dependencies
- Python 3.8.5 (or higher)

### Installation
Make sure you have installed Python version 3.8.5 or above. No other dependencies is currently needed. Usage of venv or Anaconda is recommended (but not required)

#### For Anaconda users (optional)
To quickly set up a virtual development environment with Anaconda, use the following commands in the project's root folder:
```console
conda env create -f environment.yml
conda activate ssg_env
```

### Basic Usage
Generate a website from a file or folder:
```console
python main.py --input <INPUT_FILE_OR_FOLDER>
```
Default output folder is `./dist/`, to specify a custom output folder:
```console
python main.py --input <INPUT_FILE_OR_FOLDER> --output <OUTPUT_FOLDER>
```
CSS can be used via the `--stylesheet` flag:
```console
python main.py --input <INPUT_FILE_OR_FOLDER> --stylesheet <STYLESHEET_URL>
```
For more usage, please refer to:
```console
python main.py -h
```

### License
[MIT](LICENSE)
