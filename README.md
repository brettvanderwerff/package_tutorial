# pypi_tutorial
(WIP) A tutorial for packaging projects for the Python Package Index (PyPI)

Note: All steps of this tutorial were performed on a completely fresh install of Linux Ubuntu 18.04.1 LTS, commands will vary slightly by OS and environment.

### What is a Python package?

### What is the Python Package Index? 



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
    name="package_tutorial",
    version="0.0.1",
    author="Brett Vanderwerff",
    author_email="brett.vanderwerff@gmail.com",
    description="A small example package",
    long_description='A small example package to demonstrate uploading packages to PyPI for distribution.',
    url="https://github.com/brettvanderwerff/package_tutorial",
    packages=['package_tutorial', 'package_tutorial.get_average', 'package_tutorial.get_sum'],
    install_requires=[
       'numpy'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Natural Language :: English",
        "License :: unlicense",
        "Operating System :: OS Independent",
    ),
)
```

There is a lot going on in `setup.py`, bet we can look at it piece by piece.

First we import setuptools, which is a part of the Python standard library (as far as I know) that facilitates the generation of Python packages for distribution.

setuptools has a setup method that runs the setup. 

To the setup method we pass the following arguments: 

* name: The name of our package :)
* version: Attempts have been made to standardize version schemes, its pretty complicated you can read more about that here: https://www.python.org/dev/peps/pep-0440/
* author: Your name if you made the package
* author_email: Your email if you made the package
* Description: Just a short blurb about what the package does.
* url: A url for the source code repository, these days this is almost always a repo hosted on Github
* packages: This is a list of our local packages we would like included in the distribution package. In our case this is just a list containing all the folders we have containing an `__init__.py` file. If any packages contained development tools we didn't want to distribute, we could have just excluded them from the list. You can also set `packages=find_packages()` here, which will walk the project directory and return a list of all folders containing an `__init__.py` file.
* install_requires: This is a list of dependencies. When setup.py runs, an attempt will be made to install these dependencies in your environment. 
* classifiers: Classifiers will end up being tags on PyPI that will help people search for your project.

Keep in mind that most of these arguments are just metadata that show up on the PyPI page that hosts your project.



classifiers: https://pypi.org/pypi?%3Aaction=list_classifiers

Contents of `__init__.py`:

`__init__.py` is actually just an empty file. Its really important though, placing `__init__.py` in the pypi_tutorial makes Python recognize that directory as a package, which can then be imported by Python as if it was a .py file like so:
 
 `import pypi_tutorial` 
 
 We could also import any submodules contained within the pypi_tutorial package like so:
 
 `from pypi_tutorial import my_prog`
 
 I don't think we get much benefit out of packaging our little program here, but organizing code into packages (and subpackages) becomes a very powerful way to separate out functional components of a larger code base and even some not so large code bases.
 



Contents of `myprog.py`:

```python

from package_tutorial.get_average import get_average
from package_tutorial.get_sum import get_sum

def my_prog(input_list):
    get_average.run(input_list=input_list)
    get_sum.run(input_list=input_list)

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



