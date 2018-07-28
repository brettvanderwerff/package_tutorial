# pypi_tutorial
(WIP) A tutorial for packaging projects for the Python Package Index (PyPI)

Note: All steps of this tutorial were performed on a fresh install of Linux Ubuntu 18.04, commands will vary slightly by OS and environment.


1. Clone repository

Project Structure:

```
pypi_tutorial
├──pypi_tutorial     
│   ├── __init__.py        
│   └── my_prog.py 
└── setup.py  
```

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




