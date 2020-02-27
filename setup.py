import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bibconvert",
    version="0.0.1",
    author="Songsheng Tao",
    description="A CLI program to convert citation files to a rg-db-public citation style yaml files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: ",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
