import setuptools
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pycondbx",
    version="0.0.1",
    author="PyconDev",
    author_email="@mmartin",
    description="Demo Pycon DBX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['pycondbx'],
    python_requires="==3.8.10",
)
