# package_tutorial
(WIP) A tutorial for packaging projects for the Python Package Index (PyPI)


### What is a Python package?

On one level Python packages can be thought of as folders that can be imported into Python similar to to how modules can be imported. Packages usually contain a collection of related modules that are visible to Python upon importing the package. 

### Why should I care about packaging my projects?

Organizing code into packages (and subpackages) becomes a very powerful way to separate out functional components of a larger code base and even some not so large code bases. In my experience it makes the code base easier to maintain as the project develops and it can make the project easier to share with use of the Python Package Index, as we will see with this demonstration.

### What is the Python Package Index? 

To me a large part of what makes Python so great is the community and the vast amount of open-source tools that have been developed by the community. When individuals develop tools in Python, it is common for those individuals to structure their tools as packages and distribute them to other Python users via the Python Package Index (PyPI, https://pypi.org/), a large online repository for Python packages. Anyone who wants to pull a package from PyPI to use on their personal machine can do so easily with the Python package management system "pip". At the time of writing this, there are 148,000 packages on PyPI.

### What are we going to learn here today?

We are going to learn a bit about how to package your project and upload it to PyPI. 

### Lets get started!

##### Note: All steps of this demonstration were performed on a completely fresh install of Linux Ubuntu 18.04.1 LTS, commands will vary slightly by OS and environment (but not much).


1. Open a terminal and clone the tutorial repository.

```commandline
$sudo apt install git \
git clone https://github.com/brettvanderwerff/package_tutorial

```

2. Change directory into the pypi_tutorial folder

```commandline
$cd package_tutorial
```

3. Make a python virtual environment

```commandline
$sudo apt-get install python-venv \
python3 -m venv venv

```


This command runs the Python package venv to create a virtual environment 'venv'. This virtual environment is a fresh install of the Python interpreter. This prevents us from having dependency conflicts with the system-wide Python interpreter. It really depends on what you are doing, but in some cases it is good practice to develop each of your projects with thier own virtual environment. Later we will be activating this virtual environment.


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

every `__init__.py` file in our project is just an empty file. Its really important though, placing `__init__.py` in the package_tutorial folder makes Python recognize that directory as a package, which can then be imported by Python as if it was a .py file like so:
 
 `import package_tutorial` 
 
 We could also import any modules contained within the package_tutorial package like so:
 
 `from package_tutorial import my_prog`


4. Lets have a look at the files in our example project. The program itself does not do anything special, it was just made to demonstrate packaging structure. I also made sure it had a dependency for good measure.


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

There is a lot going on in `setup.py`, but we can look at it piece by piece.

First we import setuptools, which is a tool that facilitates the generation of Python packages for distribution.

setuptools has a setup method that runs the setup. To the setup method we pass the following arguments: 

* name: The name of our package :)
* version: Attempts have been made to standardize version schemes, often they follows the format "major.minor.micro", more about that here: https://www.python.org/dev/peps/pep-0440/
* author: Your name if you made the package
* author_email: Your email if you made the package
* description: Just a short blurb about what the package does. People will see this description alongside your project name when looking through PyPI search results. 
* long description: A long blurb about what the project does, usually people set this argument equal to a string representing their entire README file.
* url: A url for the source code repository, these days this is almost always a repo hosted on Github.
* packages: This is a list of our local packages we would like included in the distribution package. In our case this is just a list containing all the folders we have containing an `__init__.py` file. If any packages contained development tools we didn't want to distribute, we could have just excluded them from the list. You can also set `packages=find_packages()` here, which will walk the project directory and return a list of all folders containing an `__init__.py` file.
* install_requires: This is a list of dependencies. When setup.py runs, an attempt will be made to install these dependencies in your environment. 
* classifiers: Classifiers will end up being tags on PyPI that will help people search for your project. Here is more info on classifiers: https://pypi.org/pypi?%3Aaction=list_classifiers

Keep in mind that most of these arguments are just metadata that show up on the PyPI page that hosts your project and help PyPI users search for your project.  

Contents of `get_average.py`:

```python
import numpy as np

def run(input_list):
    print("The average of list items is: " + str(np.average(input_list)))

```
`get_average.py` contains a function that prints the average of a list of items.

Contents of `get_sum.py`:

```python
import numpy as np

def run(input_list):
    print("The sum of list items is: " + str(np.sum(input_list)))

```
`get_sum.py` contains a function that prints the sum of a list of items.  

Contents of `myprog.py`:

```python

from package_tutorial.get_average import get_average
from package_tutorial.get_sum import get_sum

def my_prog(input_list):
    get_average.run(input_list=input_list)
    get_sum.run(input_list=input_list)

```
This is just a program that imports the `get_average` and `get_sum` modules and combines them into a single function called `my_prog`. 


Thats it for showing the project structure and contents, lets move on to uploading this package to PyPI.


5. Navigate to the top level directory and create a new python virtual environment:

```commandline
$python3 -m venv venv
```


6. Activate the virtual environment

```commandline
$source venv\bin\activate
```



7. Make sure setuptools is installed 

```commandline
$pip install -U setuptools

```

This command installs the python packages setuptools to our virtual environment. The U flag indicates that these packages will be upgraded to the most recent versions if they are already installed but outdated. 

8. Run the setup.py script to create the distribution of our package. 

```commandline
$python3 setup.py sdist
```

This command creates a folder `dist/` in our top level directory. A gzipped file including our package and some meta-data is writen in this `dist` folder. 

search : Minimally, you should create a Source Distribution in  https://packaging.python.org/guides/distributing-packages-using-setuptools/

9. Make an account on [TestPyPI](https://test.pypi.org/account/register/). This is a test instance of the real PyPI that lets us test our uploading process without affecting the real PyPI. You should walk away from this registration with a username and password. You will likely also need to verify your email with TestPyPI.

10. Make sure twine is installed

```commandline
$pip install -U twine
```
Twine is a tool for securely interfacing with PyPI/TestPyPI and uploading our package.

11. After installing twine, we will use it to upload our package by using the following command 

```commandline
$twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

This command indicates that everything in the `dist` folder that we generated by running our `setup.py` folder is to be uploaded using the url for TestPyPI.
PyPI overhauled their code-base this year, the "legacy" in the repository url is a reference to that migration and may change (https://github.com/pypa/warehouse/issues/2285). 
Assuming twine is able to form a connection, you will be prompted to enter your TestPyPI credentials. You will get an error if you did not confirm your email address with TestPyPI.

12. Once the package is successfully uploaded to TestPyPI, we can test our project by making a new project folder and virtual environment (see step 5) and see if the project works by installing our package in our activated virtual environment by using the following command: 

```commandline
$pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple package-tutorial
```

The `--index-url` flag argument indicates that we want pull our package from TestPyPI. The `--extra-url` flag argument indicates that we want to pull any of our projects dependencies that are not available on TestPyPI from the real PyPI. 

13. Test the package pulled from TestPyPI by starting the Python interpreter in your virtual environment and importing the my_prog module and running the program:

```commandline
$python3
```

and then enter into the interpreter:

```commandline
>>>from package_tutorial import my_prog
>>>my_prog.run([1,2,3,4,5,6])
The average of list items is: 3.5
The sum of list items is: 21
```
Great, looks like everything works. Lets upload this to the real PyPI.

14. Uploading to PyPI is really straight forward, we just go back to our original project folder, activate the virtual environment and upload the package to PyPI with the following command:

```commandline
$twine upload dist/*
```
Thats all there is to it. In summary PyPI increases the accessibility of your tool to others greatly. If there is ever a need to use your tool in the future you, or anyone else, can just run `pip install package_tutorial` (or whatever the name of your package is) in an environment with pip installed to collect the project from PyPI. 

#### References

1. https://packaging.python.org/tutorials/packaging-projects/
2. https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
3. https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
4. http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
5. https://packaging.python.org/guides/using-testpypi/



