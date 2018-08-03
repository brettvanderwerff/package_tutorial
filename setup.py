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