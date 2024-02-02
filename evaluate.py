import matplotlib.pyplot as plt
from engine import *
import sys


def getXValues():
    X_vector =input("Range of x values: ")
    X_vector.split()

    build_first =True
    x_1 =""
    x_2 =""

    for char in X_vector:
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            if build_first:
                x_1 +=str(char)

            else:
                x_2 +=str(char)

        elif char =="-":
            build_first =False

        else:
            print("\nevaluate.py:ERROR:Range format is strictly x(1)-x(2)\n")

    x_1 =int(x_1)
    x_2 =int(x_2)

    X_vector =list(range(x_1,x_2+1))

    return X_vector
    

def read_output(user_input, X):
    print(f"\nINPUT: {user_input}")
    print(f"X: {X}")

    with open("./output.txt") as file:
        pass


def terminal_output_y(Y):
    print("OUTPUT:")
    print(f"Y: {Y}")


def evaluate_expression(parser_data_file, X):

    Y =[]
    label_values =[]

    with open(parser_data_file, "r") as file:
        while True:
            char =file.read(1)
            if not char:
                break

            else:
                pass

    return Y


def main():
    ###################
    # CONTROL VARIABLES
    ###################
    # "w" (WRITES TO FILE UNDER write_path), "p" (PRINTS TO CONSOLE), "l" (TRANSLATES AND OVERWRITES A .lmdat FILE)
    control_char ="l"
    force_string_print =True
    show_internals =True
    parser_data_file ="./cumulative_output.txt"
    ###################

    '''
    argv =len(sys.argv)
    options =[]
    base_options =['c','g','o']
    current_options =[]
    start_option =True

    if argv ==0:
        pass

    elif argv ==1:
        options.append(sys.argv[1])

        for option in options:
            for char in option:
                
                if start_option:
                    if char =='-':
                        start_option =False

                    else:
                        print(f"evaluate.py:ERROR:Wrong options:{sys.argv[1]}")

                else:
                    if char =='c':
                        pass
                    elif char =='g':
                        pass
                    elif char =='o':
                        pass

    elif argv ==2:
        options.append(sys.argv[1])
        options.append(sys.argv[2])

    elif argv ==3:
        options.append(sys.argv[1])
        options.append(sys.argv[2])
        options.append(sys.argv[3])

    '''

    deleteCumulativeLMDAT()

    string =getInput()
    X =getXValues()

    read_output(string, X)

    tokens, values =scanner(string)

    val_buffer, opr_buffer, left_num, right_num =parser(tokens, values)

    if show_internals:
        print("\nDEBUG:\n")
        print("Tokens: ", tokens)
        print("Values: ", values)
        print("val_buffer, opr_buffer, left_num, right_num: ", val_buffer, opr_buffer, left_num, right_num, "\n")

    string =internalRepresentation(val_buffer, opr_buffer, left_num, right_num, control_char, show_internals)

    if control_char =="p":
        print("\nPARSER:\n", string, "\n")

    else:
        if force_string_print:
            print("\nPARSER:\n", string, "\n")

    Y =evaluate_expression(parser_data_file, X)

    terminal_output_y(Y)

    endLMDAT()

    return string


if __name__ =="__main__":
    main()