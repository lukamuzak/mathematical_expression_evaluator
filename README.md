# mathematical_expression_evaluator
Python code for parsing a string-form mathematical expression and evaluating it for a range of x values. Please note that this version of the project is very inefficient, and can definitely be sped up.

PROJECT STRUCTURE
-----------------
The evaluator consists of two .py files. The first (engine.py) being used to parse the expression in string form, and the other (evaluate.py) to evaluate the result of the parsing over a range of x values passed as a list.

HOW TO RUN
----------
Running the evaluator is as simple as running "$ python evaluate.py" on your command line. In this base case, the output will be a list of x values followed by a list of y values to which they are mapped to.

Input: x^2
X: [0,1,2,3,4,5,6,7,8,9,10]
Y: [0,1,4,9,16,25,49,64,81,100]
