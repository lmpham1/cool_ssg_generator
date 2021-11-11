# CONTRIBUTING.MD

### Dependencies
- [Python 3.8.5](https://www.python.org/downloads/) (or higher)

***

### Installation
Make sure you have installed Python version 3.8.5 or above. No other dependencies is currently needed.

To clone this project, use:
```console
git clone https://github.com/lmpham1/cool_ssg_generator.git
```
Then, you'll probably want to navigate to the project's root folder:
```console
cd cool_ssg_generator
```

#### Setting up the environment with Anaconda
If you want to quickly set up a virtual development environment with Anaconda, use the following commands in the project's root folder:
```console
conda env create -f environment.yml
conda activate ssg_env
```

***

### Filing An Issue
Any issue is welcome! Just make sure that you check the [list of issue](https://github.com/lmpham1/cool_ssg_generator/issues) to see if it already exists before filing.

Also, please make sure you include as much details as possible in your issues.

***

### Format Your Code with Black Formatter
This project uses [black](https://pypi.org/project/black/) for code formatting. If you set up the environment with Anaconda, `black` should already be installed in the `ssg_env` environment. Otherwise, you can install it by using:
```console
pip install black
```
***Note***: Make sure your `black` version is `21.10b0` or above

To format the code, run the following command:
```console
black .
```

Note that if you are using Visual Studio Code as your IDE, it should already format your code as you make changes to a `.py` file.

### Lint Your Code with Flake8
This project uses [Flake8](https://flake8.pycqa.org/en/latest/index.html) as a linter. If you set up the environment with Anaconda, `flake8` should already be installed in the `ssg_env` environment. Otherwise, you can install it by using:
```console
pip install flake8
```
***Note***: Make sure your `flake8` version is `4.0.1` or above

To run the linter, run:
```console
flake8 .
```
Note that if you are using Visual Studio Code as your IDE, it should already lint your code as you make changes to a `.py` file.

### Test Your Code with pytest
This project uses [pytest](https://docs.pytest.org/en/latest/) for automated testing. If you set up the environment with Anaconda, `flake8` should already be installed in the `ssg_env` environment. Otherwise, you can install it by using:
```console
pip install pytest
```
***Note***: Make sure your `pytest` version is `6.2.5` or above

All test files go into the `/tests/` folder at project's root level. Feel free to make a new test file or function if you need to. Just make sure to follow their [guidelines](https://docs.pytest.org/en/6.2.x/goodpractices.html) when you do so.

To run all test functions in a test file:
```console
pytest tests/<TEST_FILE_NAME>.py
```

To run a specific function inside a test file:
```console
pytest tests/<TEST_FILE_NAME>.py::<TEST_FILE_FUNC>
```

To run all tests:
```console
pytest
```

For more information on how to use `pytest`, please refer to their [documentation](https://docs.pytest.org/en/latest/how-to/index.html).