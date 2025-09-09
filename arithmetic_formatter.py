def arithmetic_arranger(problems, show_answers=False):
    # This is a conditonal statement based on the fcc instructions for the project in which the condition checks that if the length of problems which is a list of problems is greater than 5 and if it is  then it returns an error string and yes keep in mind that returning an error string does not carsh the program but raising an error does.
    if len(problems) > 5:
        return "Error: Too many problems."
    
    line1_list = [] # will have     32  etc
    line2_list = [] # will have  + 698  etc
    line3_list = [] # will have  -----  etc
    line4_list = [] # will have    730  etc
    
    #The loop iterates through every problem in the list of problems
    for problem in problems:
        left, operator, right = problem.split() # The split function will split the problem like this as the first problem is "32+698" now it will be "32","+","698"
      
        # This is another conditional statement based on the provided instructions and in this statement the operator must be either + or - or else the statement will return an error string 
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        # This is another function that returns an error string if the left or right operand is not a positive whole number , the isdigit function rejects all negative numbers , alphabets and boolean datatype
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."
        # Another conditional statement based on the instructions provided which checks if the length of either of the operands is greater than 4 and then returns an error string if it is 
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # max() is a function that takes two aurguments and chooses the greater one for further operations as here len("32") is 2 and len("698") is 3 and here 3 is greater so it will be added to the external 2 giving us the width to be 5 
        width = max(len(left), len(right)) + 2
        
        # Append the operands and operator to the  corresponding lists and here r.just stands for right justification which is simply used to adjust the operand or operator in the left to right direction as "32" will be formatted like this ,   32 leaving three spaces and occupying 2 spaces

        line1_list.append(left.rjust(width))
        line2_list.append(operator + right.rjust(width - 1))
        line3_list.append("-" * width) # gives us 5 of these "-" but remember that this is not an arithmetic operation

        # the show_answers was an optional parameter so if its given then the following operations will be performed to get the appropriate answer
        if show_answers:
            if operator == "+":
                answer = str(int(left) + int(right))
                # here the operator is + so we will add the operands but inorder to get the correct sum we will convert the operands into integers then back to strings again
            else:
                # same thing as the upper one but with the - sign
                answer = str(int(left) - int(right))
            line4_list.append(answer.rjust(width))

    # Join everything with 4 spaces so that the output is neat and formatted nicely and every problem after the first one has four spaces before the last one  
    arranged_problems = "    ".join(line1_list) + "\n" + "    ".join(line2_list) + "\n" + "    ".join(line3_list)
    if show_answers:
        arranged_problems += "\n" + "    ".join(line4_list)

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
