# BACO APP: Attrition Analysis Universidad de Boyacá

Team 56 final project for Data Science 4 All / Colombia 2021

### Relevant links

* [Google Drive Shared Folder](https://drive.google.com/drive/folders/1R9QG7rAmjnp3hWU2ty4xIT6LB6aRHti-)
* [Notion Project Tracker](https://www.notion.so/Team-56-Project-Tracker-e725562bd9cb47b9910e6ef96452ab09)
* [Trello Kanban Board](https://trello.com/b/Ga8QCmGz)

## Requirements
* [`python`](https://www.python.org/downloads/) 3.3.x or greater
* `pip`

## Table Of Contents

1. **[Instructions For Developers](#instructions-for-developers)**<br>
    1. [Naming Convention](#naming-convention)<br>
    2. [Dependencies Installation](#dependencies-installation)<br>

# Instructions For Developers

To work on the project you need to: 

* Clone the project to your computer
* Install dependencies
* Use branches, Never work  directly on `main` or `dev` branches
* Follow the naming convention

You can find detailed instructions below.

## Naming Convention

As you create new directories and files, use names that make it easier for anyone to find things and also to understand what each files does or contains.

Use file and directory names that are:

* **Human readable:** use expressive names that clearly describe what the directory or file contains (e.g. code, data, outputs, figures).
* **Machine readable:** avoid strange characters and spaces. Instead of spaces, use `_` to separate words.
* **Consistent:** always use lower case (It might be tempting to use `lower` and `Upper` case. However, case will cause coding issues, particularly when switching between operating systems)

### Jupyter notebooks Naming Convention

a number (for ordering), the creator's initials, and an underscore `_` delimited description, e.g.
    
    `01_jpj_initial_data_exploration.ipynb`


## Dependencies Installation

The easy way to get the dependecies would be to just run `pip install -r requirements.txt` (global installation), The proper (and recomended) way is to use a virtual enviroment. The steps to do so ares explained below.

### Create new virtual environment

The following command creates a new virtual environment directory named `.venv` in the current directory (project's directory).
```sh
python -m venv .venv
```

### Activate virtual environment

To start using this virtual environment, you first need to activate it. The following commands activate an existing virtual environment on Windows and Unix systems. However, it would be easier if you set up your editor or IDE to activate virtual enviroments for you it for you.

Windows CMD:
```sh
.venv\Scripts\activate.bat
```

Windows PowerShell:
```sh
.venv\Scripts\activate.ps1
```

Unix (Linux and Mac OS):
```sh
source ./.venv/bin/activate
```
Once the virtual environment has been activated, your console cursor might prepend the name of the virtual environment.

It will look similar to this:
```sh
(.venv) $ echo 'Hello World!'
```

### Deactivate virtual environment

The following command deactivates the current virtual environment, any dependency installed after this command will be installed globally.
```sh
deactivate
```

### Installing Dependencies

`requirements.txt` contains a list of all the dependencies needed for the project to work. To install dependencies in the current environment from a `requirements.txt` file, the command below can be used.
```sh
pip install -r requirements.txt
```

### adding new dependencies

(Do not do this if you are not using a virtual enviroment).

To install a new individual package:

```sh
python -m pip install <PACKAGE>
```

To create or update a requirements file from the current environment, run the following command while the virtual environment is active. This will create a file called `requirements.txt` in the current directory. 

```sh
pip freeze > requirements.txt
```

### Team
* **Paola Rojas Castañeda:** [@gpaolarojas](https://github.com/gpaolarojas)
* **Manuela Escobar:** [@manuelaescobar](https://github.com/manuelaescobar)
* **Alejandro Marin:** [@almarinca](https://github.com/almarinca)
* **Alvaro Guijarro:** [@Alvaroguijarro97](https://github.com/Alvaroguijarro97)
* **Alejandro Hurtado:** [@falejo](https://github.com/Falejo)
* **Ricardo Ibarra:** [@ricardo8aib](https://github.com/ricardo8aib)
