import setuptools

setuptools.setup(
    name="pypi_tutorial",
    version="0.0.1",
    author="Brett Vanderwerff",
    author_email="brett.vanderwerff@gmail.com",
    description="A small example package",
    url="https://github.com/cougpy/pypi_tutorial",
    packages=['pypi_tutorial'],
    install_requires=[
       'numpy'
    ],
    entry_points={
        'console_scripts' : [
            'pypi_tutorial = pypi_tutorial.__main__:main'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Natural Language :: English",
        "License :: unlicense",
        "Operating System :: OS Independent",
    ),
)