import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unravel",
    version="0.0.1",
    author="Mark Cottman-Fields",
    author_email="cofiem@gmail.com",
    description="A command-line interface and core library for indexing, analysing, and comparing laws, EULAs, ToSs, Privacy Policies, and other legal documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/unravel-text/unravel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)