[![Language Python](https://img.shields.io/badge/Linguagem-Python-blue.svg)]()

# Installing requirements

### Requirements:

- Python 3.9 or newer.

- Pip

### Checking Python version:
```sh
$ python -V
or
$ python --version
```
### Checking Pip version:
```sh
$ pip -V
ou
$ pip --version
```
### Installing VirtualEnv
```sh
$ pip install virtualenv
```
After installing virtualenv we need to initialize the enviroment.
So we are going to create the ```venv``` folder and initialize it:
```sh
$ mkdir venv
$ python3 -m venv venv
```
Now we must activate it:
```sh
$ source venv/bin/activate
```
To deactivate, simply execute:
```sh
$ deactivate
```
### Installing project dependencies:
All the requirements are in requirements.txt.
```sh
$ pip install requirements.txt
```