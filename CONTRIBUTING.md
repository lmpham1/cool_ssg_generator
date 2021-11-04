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
```
pip install black
```

To format the code, run the following command:
```console
black .
```