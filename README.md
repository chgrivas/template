# Description
***
This is a README file in markdown format for the project that can be used as a python template.

## Project Structure
***
### setup.py

This is the file containing the project's initial setup and it is used by packaging and distribution making commands.

The setup method may contain:

* name
* version
* author
* author_email
* description
* license
* url
* packages
* long_description
* py_modules
* classifiers

### ez_setup.py

This python script includes functions that deal with transparent setuptools downloading. These functions are imported and used in the beginning of the setup.py file.

### template/

The folder named after the project name. It should be containing the source code organized in packages. It is a package too!

### tests/

The folder containing every file that has to do with "the testing suite".

More info can be found in the tests/README.md file.

### AUTHORS

A comprehenive list of the project's authors & contributors.

### LISENCE

C'mon, it's obvious...

### .gitignore

A file that excludes some files or some file groups from git versioning tools.

## Useful commands
***
### General
`python setup.py install`  
`python setup.py sdist`

### pip
`pip freeze`

### Testing
`python -m unittest discover`

### Style guidelines checking
`flake8 template`

## Links
***
[Style Guide for Python code](http://legacy.python.org/dev/peps/pep-0008/)

