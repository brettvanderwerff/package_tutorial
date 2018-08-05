# pypi_tutorial
(WIP) A tutorial for packaging projects for the Python Package Index (PyPI)


### What is a Python package?

On one level Python packages can be thought of as folders that can be imported into Python similar to to how modules can be imported. Packages usually contain a collection of related submodules that are visible to Python upon importing the package. 

### Why should I care about packaging my projects?

Organizing code into packages (and subpackages) becomes a very powerful way to separate out functional components of a larger code base and even some not so large code bases. In my experience it makes the code base easier to maintain as the project develops and it can make the project easier to share with use of the Python Package Index, as we will see with this demonstration.

### What is the Python Package Index? 

To me a large part of what makes Python so great is the community and the vast amount of open-source tools that have been developed by the community. When individuals develop tools in Python, it is common for those individuals to structure their tools as packages and distribute them to other Python users via the Python Package Index (PyPI, https://pypi.org/), a large online repository for Python packages. Anyone who wants to pull a package from PyPI to use on their personal machine can do so easily with the Python package management system "pip". At the time of writing this, there are 148,000 packages on PyPI.

### What are we going to learn here today?

We are going to learn a bit about how to package your project and upload it to PyPI. 


##### Note: All steps of this demonstration were performed on a completely fresh install of Linux Ubuntu 18.04.1 LTS, commands will vary slightly by OS and environment (but not much).


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
package_tutorial
│
├──package_tutorial     
│   ├── __init__.py   
│   │    
│   ├──get_average
│   │   ├──__init__.py
│   │   └──get_average.py
│   │
│   ├──get_sum
│   │   ├──__init__.py
│   │   └──get_sum.py
│   │
│   └── my_prog.py 
│
└── setup.py  
```

Its important to note that we have 3 packages here: the top level package_tutorial along with get_average and get_sum. Packages are identified as folders that contain an `__init__.py` file. 


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
* description: Just a short blurb about what the package does. People will see this description alongside your project name when looking through PyPI search results. 
* long description: A long blurb about what the project does, usually people set this argument equal to a string representing their entire README file.
* url: A url for the source code repository, these days this is almost always a repo hosted on Github.
* packages: This is a list of our local packages we would like included in the distribution package. In our case this is just a list containing all the folders we have containing an `__init__.py` file. If any packages contained development tools we didn't want to distribute, we could have just excluded them from the list. You can also set `packages=find_packages()` here, which will walk the project directory and return a list of all folders containing an `__init__.py` file.
* install_requires: This is a list of dependencies. When setup.py runs, an attempt will be made to install these dependencies in your environment. 
* classifiers: Classifiers will end up being tags on PyPI that will help people search for your project.

Keep in mind that most of these arguments are just metadata that show up on the PyPI page that hosts your project. Here is more info on classifiers: https://pypi.org/pypi?%3Aaction=list_classifiers

Contents of `__init__.py`:

```python

```

`__init__.py` every `__init__.py` file in our project is actually just an empty file. Its really important though, placing `__init__.py` in the package_tutorial folder makes Python recognize that directory as a package, which can then be imported by Python as if it was a .py file like so:
 
 `import package_tutorial` 
 
 We could also import any submodules contained within the package_tutorial package like so:
 
 `from package_tutorial import my_prog`
 

Contents of `myprog.py`:

```python

from package_tutorial.get_average import get_average
from package_tutorial.get_sum import get_sum

def my_prog(input_list):
    get_average.run(input_list=input_list)
    get_sum.run(input_list=input_list)

```

Contents of `get_average.py`:

```python
import numpy as np

def run(input_list):
    print("The average of list items is: " + str(np.average(input_list)))

```
This is just a function that prints the average of a list of items.

Contents of `get_sum.py`:

```python
import numpy as np

def run(input_list):
    print("The sum of list items is: " + str(np.sum(input_list)))

```
This is just a function that prints the sum of a list of items. 

That it for showing the project structure and contents, lets move on to uploading this package to PyPI.


2. Navigate to the top level directory and create a new python virtual environment:

`$ python -m venv venv` 

3. Activate the virtual environment

`$source venv\bin\activate`

4. Install setuptools and twine

`$pip install -U setuptools`

This command installs the python packages setuptools to our virtual environment. The U flag indicates that these packages will be upgraded to the most recent versions if they are already installed but outdated. 

5. Run the setup.py script to create the distribution of our package. 

`$python setup.py bdist`

This command creates a folder `dist/` in our top level directory. A gzipped file including our package and some meta-data is writen in this `dist` folder. 

search : Minimally, you should create a Source Distribution in  https://packaging.python.org/guides/distributing-packages-using-setuptools/

#### References

1. https://packaging.python.org/tutorials/packaging-projects/
2. https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
3. https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
4. http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html



