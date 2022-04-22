# EHR cumulative project

This project is about developing a Python module that provides some simple analytical capabilities on some (synthetic) EHR data with suite of tests in our EHR library using the pytest framework, for all of the functions in our module. 

# For end users:

## Setup/installation instructions:
 * Pip install Datetime : 
    This is needed for the function `num_older_than(age: int, data: [[]]) -> int:` it takes the data and returns the number of patients older than a given age (in       years).
 
There's suite of tests in our EHR library using the pytest framework, for all functions, inorder to run the pytest please install the package:
 * Pip install pytest
 
 For SQL access: 
 * Pip install sqllite3


  ## Testing instructions
   * To run the file, type python assingmentone.py in the terminal.
   * To run pytest, type pytest assingmentone.py in the terminal. Make sure pytest package is installed.
   
