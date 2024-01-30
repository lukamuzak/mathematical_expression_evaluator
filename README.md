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
Y: [0,1,4,9,16,25,36,49,64,81,100]

Additionaly, you can also pass additional arguments to the evaluator. These are used to output the parsed data, turn on the parser debug output, and to turn on a graphing option.

To output the parsed data in a *esoteric* data format, which is stored as a simple .txt file in the project directory, simply write "$ python evaluate.py -o". To turn on parser debug output, use "$ python evaluate.py -c".To turn on the graphing option, use the following: "$ python evaluate.py -g". You can also combine the two options the same way as you would with a bash/zsh tool: "$ python evaluate.py -ocg".

When the -c option is used, the output looks like:

Input: x^2
X: [0,1,2,3,4,5,6,7,8,9,10]
Y: [0,1,4,9,16,25,36,49,64,81,100]

Debug:
->Tokens: []
->Values: []
->val_buffer, opr_buffer, left_num, right_num []



WHY IT WORKS
------------
When you input a string expression to the engine, say "$Enter String: x^2+2", what happens first is that the parser function checks that all of the characters (chars) in the expression are "legal", given what the char is, and what chars preceding it where. For example, if we modify the example to "$Enter String: (+x^2+2)", we will get an error at the second char (index 1), because putting a plus sign in front of a open bracket is unnecessary. Continuing with the first example, given that there will be no error generated, what happens next is that the entire expression string is parsed to generate a binary vector. In our case, the binary vector generated is [1,0]. In any expression, the algorithm then searches for a pattern of 1 (if the expression size is 3, not counting brackets) or "1,0", if larger than 3. The reasoning behind this pattern search is the following: 1 signals that the current char is a mathematical operation symbol (+,-,*,^,/) and has a higher priority than the one 

FINAL NOTE
----------
Thank you for checking out and downloading the repository! I can be reached at luka.muzak@gmail.com
