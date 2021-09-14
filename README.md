# cool_ssg_generator
A simple SSG generator made with Python.
Current version is 0.1

### Dependencies
- Python 3.8.5

### Installation
Make sure you have installed Python version 3.8.5 or above

No other dependencies is currenly in used. For easy installation of dependencies in the future, usage of Anaconda is recommended. To set up the development environment with Anaconda:
```console
conda env create --file environment.yml
```
Then, activate the newly created environment:
```console
conda activate ssg_env
```
Alternatively, you can install dependencies using _pip/pip3_

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
