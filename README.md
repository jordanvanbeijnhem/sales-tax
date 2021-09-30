This project contains the code for assessment #2: Sales taxes

# Running the code
In order to run the tests, you can use the following command in the root directory of the project:
`python -m unittest`.
This command will run the tests that are specified in tests.py, which is a representation of the test
cases supplied in the assessment description.

# Structure of the project
The code is split into several files, for better readability. The representations of the shopping basket and shopping basket item can be
found in the models.py, the code responsible for the parsing of a string into a shopping basket item model, can be found
in parsers.py, the tests are in tests.py, the exception that can be raised during parsing is in exceptions.py and finally,
the method to correctly round the sales tax can be found in utils.py.