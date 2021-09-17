# cool_ssg_generator
A simple SSG generator made with Python.
Current version is 0.1.0

### Dependencies
- [Python 3.8.5](https://www.python.org/downloads/) (or higher)

### Installation
Make sure you have installed Python version 3.8.5 or above. No other dependencies is currently needed.

To clone this project, use:
```console
git clone https://github.com/lmpham1/cool_ssg_generator.git
```

#### For Anaconda users (optional)
To quickly set up a virtual development environment with Anaconda, use the following commands in the project's root folder:
```console
conda env create -f environment.yml
conda activate ssg_env
```
For more information on Anaconda, please refer to their [official documentation](https://docs.anaconda.com/)

### Basic Usage
Navigate to the project folder:
```console
cd cool_ssg_generator
```
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
