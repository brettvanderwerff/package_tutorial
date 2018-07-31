# pypi_tutorial
(WIP) A tutorial for packaging projects for the Python Package Index (PyPI)

Note: All steps of this tutorial were performed on a completely fresh install of Linux Ubuntu 18.04.1 LTS, commands will vary slightly by OS and environment.


1. Open a terminal and clone the tutorial repository.

```commandline
$sudo apt install git \
git clone https://github.com/brettvanderwerff/pypi_tutorial

```

2. Change directory into the pypi_tutorial folder

```commandline
$cd pypi_tutorial
```

3. Make a python virtual environment

```commandline
$sudo apt-get install python3-venv \
python3 -m venv venv

```


This command runs the Python package venv to create a virtual environment 'venv'. This virtual environment is a fresh install of the Python interpreter. This prevents us from having dependency conflicts with the system-wide Python interpreter. I think its good practice to develop each of your projects with thier own virtual environment. Later we will be activating this virtual environment.


Project Structure:

```
pypi_tutorial/
├──pypi_tutorial/     
│   ├── __init__.py        
│   └── my_prog.py 
└── setup.py  
```

4. Have a look at all the 

Contents of `setup.py`:

```python
import setuptools

setuptools.setup(
    name="pypi_tutorial",
    version="0.0.1",
    author="Brett Vanderwerff",
    author_email="brett.vanderwerff@gmail.com",
    description="A small example package",
    url="https://github.com/cougpy/pypi_tutorial",
    packages=setuptools.find_packages(),
    install_requires=[
       'numpy'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

```
classifiers: https://pypi.org/pypi?%3Aaction=list_classifiers

Contents of `__init__.py`

```python
name = "pypi_tutorial"

```

Contents of `myprog.py`:

```python

```

2. Navigate to the top level directory and create a new python virtual environment:

`$ python -m venv venv` 

3. Activate the virtual environment

`$source venv\bin\activate`

4. Install wheel and twine

`$pip install wheel, twine`


#### References

1. https://packaging.python.org/tutorials/packaging-projects/
2. https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
3. https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
4. http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html



