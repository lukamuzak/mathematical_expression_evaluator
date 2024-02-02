# CODE FOR SCANNING AND PARSING EQUATIONS


def getInput():

    expression =input("Enter string: ")
    return expression


def scanner(string):

    string =string +" "
    tokens =[]
    values =[]
    buffer =""
    index =-1
    dot_flag =False
    state =""

    for char in string:
        index +=1

        if char in ['0','1','2','3','4','5','6','7','8','9']:
            state ='num'
            buffer =buffer +char

        elif char ==".":
            if state =='num':
                dot_flag =True
                buffer =buffer +char

            else:
                raise(ValueError(f"Scanner state error at index {index}"))
            
            state ="dot"

        else:
            if state =="num":
                if dot_flag ==False:
                    values.append(int(buffer))
                    tokens.append("num")

            elif state =="dot":
                raise(ValueError(f"Scanner state error at index {index}"))
            
            if dot_flag ==True:
                values.append(float(buffer))
                tokens.append("num")

            state =""
            dot_flag =False
            buffer =""
            tokens.append(char)
            values.append(" ")

    return tokens, values

            
def parser(tokens, values):

    state =""

    # CONTEXT DATA
    val_buffer =[]
    opr_buffer =[]

    left_num =[]
    right_num =[]

    left_brackets =0
    right_brackets =0
    #

    char =tokens[0]
    tokens =tokens[1:]

    if char =="num":
        state ="num"
        left_num.append(0)

    elif char =="x":
        state ="x"
        left_num.append(0)

    elif char =="(":
        left_brackets +=1
        state ="("

    else:
        raise(ValueError("Char at index 0 leads to error state"))
    
    index =-1

    for char in tokens:
        index +=1

        if char ==" ":
            if state =="num":
                val_buffer.append(values[index])
                right_num.append(0)

            elif state =="x":
                val_buffer.append(state)
                right_num.append(0)

            break
        
        if state =="num":
            val_buffer.append(values[index])

            if char =='^':
                state ="^"
                right_num.append(0)
                opr_buffer.append(state)

            elif char == '*':
                state ="*"
                right_num.append(0)
                opr_buffer.append(state)
            
            elif char =='/':
                state ="/"
                right_num.append(0)
                opr_buffer.append(state)
            
            elif char =="+":
                state ="+"
                right_num.append(0)
                opr_buffer.append(state)

            elif char =="-":
                state ="-"
                right_num.append(0)
                opr_buffer.append(state)

            elif char =='m':
                state ="m"
                right_num.append(0)
                opr_buffer.append(state)

            elif char =='f':
                state ="f"
                right_num.append(0)
                opr_buffer.append(state)

            elif char ==")":
                right_brackets +=1
                state =")"

                right_num.append(1)

                if left_brackets ==0:
                    raise(ValueError(f"Unclosed brackets at index {index} leads to error state (num)"))

            else:
                raise(ValueError(f"Char at index {index} leads to error state (num)"))
            

        
        elif state =="x":
            val_buffer.append(state)

            if char =='^':
                state ="^"
                right_num.append(0)
                opr_buffer.append(state)

            elif char == '*':
                state ="*"
                right_num.append(0)
                opr_buffer.append(state)

            elif char =='/':
                state ="/"
                right_num.append(0)
                opr_buffer.append(state)
            
            elif char =="+":
                state ="+"
                right_num.append(0)
                opr_buffer.append(state)

            elif char =="-":
                state ="-"
                right_num.append(0)
                opr_buffer.append(state)

            elif char =='m':
                state ="m"
                right_num.append(0)
                opr_buffer.append(state)

            elif char =='f':
                state ="f"
                right_num.append(0)
                opr_buffer.append(state)

            elif char ==")":
                right_brackets +=1
                state =")"

                right_num.append(1)

                if left_brackets ==0:
                    raise(ValueError(f"Unclosed brackets at index {index} leads to error state (num)"))

            else:
                raise(ValueError(f"Char at index {index} leads to error state (num)"))
            
        elif state =="(":

            if char =="num":
                state ="num"

                left_num.append(1)

            elif char =="x":
                state ="x"

                left_num.append(1)

            elif char =="(":
                left_brackets +=1
                state ="("
            
            else:
                raise(ValueError(f"Char at index {index} leads to error state (\"(\")"))

        elif state ==")":

            if char == '^':
                state ="^"
                opr_buffer.append(state)
            
            elif char =="*":
                state ="*"
                opr_buffer.append(state)
            
            elif char =="/":
                state ="/"
                opr_buffer.append(state)

            elif char =="+":
                state ="+"
                opr_buffer.append(state)

            elif char =="-":
                state ="-"
                opr_buffer.append(state)

            elif char =="m":
                state ="m"
                opr_buffer.append(state)

            elif char =="f":
                state ="f"
                opr_buffer.append(state)

            elif char ==")":
                right_brackets +=1
                state =")"

            else:
                raise(ValueError(f"Char at index {index} leads to error state (\")\")"))

        elif state =="^":
            if char =="num":
                state ="num"

                left_num.append(0)

            elif char =="x":
                state ="x"

                left_num.append(0)

            elif char =="(":
                left_brackets +=1
                state ="("
            
            else:
                raise(ValueError(f"Char at index {index} leads to error state (^)"))
        
        elif state =="*":
            if char =="num":
                state ="num"

                left_num.append(0)

            elif char =="x":
                state ="x"

                left_num.append(0)
            
            elif char =="(":
                left_brackets +=1
                state ="("

            else:
                raise(ValueError(f"Char at index {index} leads to error state (*)"))
            
        elif state =="/":
            if char =="num":
                state ="num"

                left_num.append(0)

            elif char =="x":
                state ="x"

                left_num.append(0)

            elif char =="(":
                left_brackets +=1
                state ="("
            
            else:
                raise(ValueError(f"Char at index {index} leads to error state (/)"))
            
        elif state =="+":
            if char =="num":
                state ="num"

                left_num.append(0)

            elif char =="x":
                state ="x"

                left_num.append(0)

            elif char =="(":
                left_brackets +=1
                state ="("
            
            else:
                raise(ValueError(f"Char at index {index} leads to error state (+)"))
            
        elif state =="-":
            if char =="num":
                state ="num"

                left_num.append(0)

            elif char =="x":
                state ="x"

                left_num.append(0)

            elif char =="(":
                left_brackets +=1
                state ="("
            
            else:
                raise(ValueError(f"Char at index {index} leads to error state (-)"))
            
        elif state =="m":
            if char =="num":
                state ="num"

                left_num.append(0)

            elif char =="x":
                state ="x"

                left_num.append(0)

            elif char =="(":
                left_brackets +=1
                state ="("
            
            else:
                raise(ValueError(f"Char at index {index} leads to error state (m)"))
            
        elif state =="f":
            if char =="num":
                state ="num"

                left_num.append(0)

            elif char =="x":
                state ="x"

                left_num.append(0)

            elif char ==")":
                right_brackets +=1
                state =")"

            elif char =="(":
                left_brackets +=1
                state ="("
            
            else:
                raise(ValueError(f"Char at index {index} leads to error state (f)"))
            
    if left_brackets ==right_brackets:
        return val_buffer, opr_buffer, left_num, right_num

    else:
        raise(RuntimeError("Number of open and closed parentheses does not match"))
    

def internalRepresentation(val_buffer, opr_buffer, left_num, right_num, control_char, show_internals):

    write_path ="/Users/lukamuzak/Desktop/luka_utilities/function_visualisation/compiled_expression.py"

    opr_buffer.append(" ")

    string =""
    original_left_num =left_num
    original_right_num =right_num

    if show_internals:
        print("->internalRepresentation() [OUT OF LOOP]: original_left_num, original_right_num", original_left_num, original_right_num)

    if len(val_buffer) ==1:
        string +=f"r={val_buffer[0]}"

        if control_char =="w":
            with open(write_path, 'a') as file:
                file.write(f"rh={val_buffer[0]}")
        elif control_char =="l":
            serialize_parsed_data(string, val1, " ")
            translateLMDAT(string, val1, " ")

    elif len(val_buffer) ==2:
        sopr =operatorString(opr_buffer[0])
        string +=f"rh={sopr}({val_buffer[0]},{val_buffer[1]})"

        if control_char =="w":
            with open(write_path, 'a') as file:
                file.write(f"rh={sopr}({val_buffer[0]},{val_buffer[1]})")
        elif control_char =="l":
            serialize_parsed_data(string, val_buffer[0], val_buffer[1])
            translateLMDAT(string, val_buffer[0], val_buffer[1])

    else:

        executable_names =0

        while(True):
            
            left_num =original_left_num
            right_num =original_right_num

            print("->internalRepresentation() [TOP OF LOOP]: left_num, right_num ", left_num, right_num)

            # ESCAPE IF THERE ARE ONLY TWO VALUES LEFT
            if len(val_buffer) ==2:
                val1, val2 =val_buffer
                opr =opr_buffer[0]
                sopr =operatorString(opr)

                string +=f"\nrh={sopr}({val1},{val2})"

                if control_char =="w":
                    with open(write_path, 'a') as file:
                        file.write(f"\nrh={sopr}({val1},{val2})")

                elif control_char =="l":
                    serialize_parsed_data("\nrh={sopr}({val1},{val2})", val1, val2)
                    translateLMDAT(f"\nrh={sopr}({val1},{val2})", val1, val2)

                break

            # RANK THE OPERATORS
            ranked_arr =[0]
            index =-1

            for opr1 in opr_buffer:
                index +=1
                opr2 =opr_buffer[index +1]

                if opr2 ==" ":
                    break

                first, second =operatorRanks([opr1,opr2])
                if first ==second:
                    ranked_arr.append(1)
                else:
                    if first >second:
                        ranked_arr.append(1)
                    
                    else:
                        ranked_arr.append(0)
            
            # UPDATE THE LEFT BRACKETS
            # DC 1
            index =-1
            power_flag =False

            for ropr in ranked_arr:
                index +=1

                if ropr ==0:
                    if right_num[index] ==0:
                        left_num[index] =1
                    
                    power_flag =False
                
                else:
                    if power_flag:
                        if right_num[index] ==0:
                            left_num[index] =1

                    power_flag =True

            left_num[-1] =0

            if show_internals:
                print("->internalRepresentation [DC 1]: left_num, right_num ", left_num, right_num)

            # PARSE THE LEFT BRACKETS FOR EXECUTABLES
            index =-1
            executable_indices =[]
            executable_name_length =0

            for br in left_num:
                index +=1

                if br ==1 and left_num[index +1] ==0:
                    executable_indices.append(index)
                    executable_name_length +=1

            # TRANSLATE THE TERMINALS
            # DC 2
            index =executable_name_length

            for i in executable_indices:
                index =index -1
                val1 =val_buffer[i]
                val2 =val_buffer[i +1]
                opr =opr_buffer[i]

                sopr =operatorString(opr)

                string +=f"\nr{executable_names +executable_name_length -index}={sopr}({val1},{val2})"

                if control_char =="w":
                    with open(write_path, 'a') as file:
                        file.write(f"\nr{executable_names +executable_name_length -index}={sopr}({val1},{val2})")
                    
                elif control_char =="l":
                    serialize_parsed_data(f"\nr{executable_names +executable_name_length -index}={sopr}({val1},{val2})", val1, val2)
                    translateLMDAT(f"\nr{executable_names +executable_name_length -index}={sopr}({val1},{val2})", val1, val2)
                
            if show_internals:
                print("->internalRepresentation [DC 2]: left_num, right_num ", left_num, right_num)

            # UPDATE THE ARRAYS
            # DC 3
            index =executable_name_length
            offset =0

            for i in executable_indices:
                
                index =index -1

                val_buffer[i -offset] =f"r{executable_names +executable_name_length -index}"
                del val_buffer[i +1 -offset]
                del opr_buffer[i -offset]

                original_left_num[i -offset] =0
                original_right_num[i -offset] =0

                del original_left_num[i +1 -offset]
                del original_right_num[i +1 -offset]

                offset +=1

            if show_internals:
                print("->internalRepresentation() [DC 3]: original_left_num, original_right_num ", original_left_num, original_right_num)

            executable_names +=executable_name_length

            if show_internals:
                print("->internalRepresentation(): executable_names, ranked_arr, left_num, right_num: ", executable_names, ranked_arr, left_num, right_num, "\n")

    return string
    

def operatorRanks(operators):

    index =-1
    operator_values =[0,0]

    for opr in operators:
        index +=1

        if opr =="^":
            operator_values[index] =6

        elif opr =="*":
            operator_values[index] =5

        elif opr =="/":
            operator_values[index] =4

        elif opr =="m":
            operator_values[index] =3

        elif opr =="f":
            operator_values[index] =2

        elif opr in ["+","-"]:
            operator_values[index] =1

    return operator_values


def operatorString(opr):

    if opr =="^":
        sopr ="exp"

    elif opr =="*":
        sopr ="mut"

    elif opr =="/":
        sopr ="div"

    elif opr =="m":
        sopr ="mod"

    elif opr =="f":
        sopr ="floor"

    elif opr =="+":
        sopr ="add"

    else:
        sopr ="sub"

    return sopr


def translateLMDAT(string, val1, val2):

    lmdat_path ="./output.txt"
    lmdat_path_cumulative ="./cumulative_output.txt"

    s1 =string[2]

    if val2 ==" ":
        with open(lmdat_path, "a") as file:
            file.write(s1 +"n")
        with open(lmdat_path_cumulative, "a") as file:
            file.write(s1 +"n")
    
    else:
        s2 =string[4]
        s3 =string[5]

        if s2 =="e":
            s4 ="0"

        elif s2 =="m":
            if s3 =="u":
                s4 ="1"
            
            else:
                s4 ="3"
            
        elif s2 =="d":
            s4 ="2"

        elif s2 =="f":
            s4 ="4"

        elif s2 =="a":
            s4 ="5"

        elif s2 =="s":
            s4 ="6"

        elif s2 =="h":
            s4 ="7"

        with open(lmdat_path, "a") as file:
            val1 =str(val1)
            val2 =str(val2)

            string =s1 +s4 +val1 +"/" +val2
            file.write(string)

        with open(lmdat_path_cumulative, "a") as file:
            val1 =str(val1)
            val2 =str(val2)

            string =s1 +s4 +val1 +"/" +val2
            file.write(string)


def serialize_parsed_data(string, val1, val2):

    current_file_path ="./output.txt"
    cumulative_file_path ="./cumulative_output.txt"

    with open(current_file_path, "a") as file:
        file.write(string[1])
        file.write(",")

        #Encode the operations as numbers (opr_0 for the first letter of the operand)
        opr_0 =string[3]
        opr_1 =string[4]

        if opr_0 =="e":
            file.write(0)

        elif opr_0 =="m":
            if opr_1 =="u":
                file.write(1)
            
            else:
                file.write(3)
            
        elif opr_1 =="d":
            file.write(2)

        elif opr_1 =="f":
            file.write(4)

        elif opr_1 =="a":
            file.write(5)

        elif opr_1 =="s":
            file.write(6)

        elif opr_1 =="h":
            file.write(7)


def endLMDAT():

    with open("./output.txt", "a") as file:
        file.write("END")
        file.close()

    
def deleteCumulativeLMDAT():

    with open("./cumulative_output.txt", "w") as file:
        file.write("")
        file.close()
