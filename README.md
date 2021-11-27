# Overview
Fmask for L2A SR, adapted from [python-fmask](https://github.com/ubarsc/python-fmask)

Please visit the main web page at: [www.pythonfmask.org](http://www.pythonfmask.org/)

Normally, the C-extension for Python package could be organized and packaged in the main package (here, 
The C-extension dependencies are located in [py-fmask-l2a](https://github.com/smile4lee/py-fmask-l2a)). However, we encountered "import errors" when we tried to debug in the IDEA. So, we build a separate ext-module for the extensions.

# Installation
To install python-fmask from the source code bundle, use the following commands

The installation uses Python's distutils packaging, so the following commands are fairly standard. 

1. Build the code
```bash
cd python-fmask-0.4.2
python setup.py build
```



2. If all goes well with that, then install. To install in default locations, just use
```bash
python setup.py install
```

3. If you wish to install in a non-default location, use
```bash
python setup.py install --prefix=/yourChosenDirectory
```

4. If installed in a non-default location, you will then need to ensure that the right environment
variables are set. For simple bash syntax, this would be something like:
```bash
export PATH="/yourChosenDirectory/bin:$PATH"
export PYTHONPATH="/yourChosenDirectory/lib/python2.7/site-packages:$PATH"
```
Note that the python2.7 sub-directory needs to match your version of python. 

