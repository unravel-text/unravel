"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://packaging.python.org/overview/
"""
import os
import re

import setuptools

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), "rt") as fh:
    long_description = fh.read()

with open(os.path.join(here, 'unravel', '_version.py'), "rt") as version_file:
    version = None
    for line in version_file:
        match = re.match("__version__ = '([^']+)'", line)
        if match:
            version = match.group(1)

    if version is None:
        raise ValueError('no version available')

setuptools.setup(
    name="unravel",
    version=version,
    author="Mark Cottman-Fields",
    author_email="cofiem@gmail.com",
    url="https://github.com/unravel-text/unravel",
    description="A command-line interface and core library for indexing, analysing, "
                "and comparing laws, EULAs, ToSs, Privacy Policies, and other legal documents.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(exclude=['docs', 'tests']),
    license="Apache Software License",
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Natural Language :: English",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords='legal natural-language command-line',
    project_urls={
        'Documentation': 'https://github.com/unravel-text/unravel/wiki',
        'Source': 'https://github.com/unravel-text/unravel',
        'Issues': 'https://github.com/unravel-text/unravel/issues',
    },
    install_requires=[
        'nltk', 'pyphen', 'spacy', 'pyphen',
        'celery',
        'country_list',
        'numpy',
    ],
    extras_require={
            'dev': ['check-manifest', 'mypy', 'bumpversion'],
            'test': ['coverage', 'check-manifest', 'readme_renderer', 'readme_render[md]', 'flake8', 'docutils', 'twine'],
    },
    entry_points={
        'console_scripts': [
            'unravel=unravel.__main__:main',
        ],
    },
)
