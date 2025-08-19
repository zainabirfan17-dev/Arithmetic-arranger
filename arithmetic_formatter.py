def arithmetic_arranger(problems, show_answers=False): 
    # Check if the number of problems exceeds the allowed limit (5)
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Lists to hold each line of the arranged problems
    line1_list = []  # Top numbers
    line2_list = []  # Operators and bottom numbers
    line3_list = []  # Dashes
    line4_list = []  # Answers (if requested)
    
    # Process each problem individually
    for problem in problems:
        # Split the problem into left operand, operator, and right operand
        left, operator, right = problem.split()
      
        # Validate operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        # Validate that both operands are digits
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Validate the length of the numbers (max 4 digits)
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Determine the width of the problem:
        # +2 accounts for the operator and at least one space
        width = max(len(left), len(right)) + 2
        
        # Right-align the top number with calculated width
        line1_list.append(left.rjust(width))
        # Right-align the bottom number with operator in front
        line2_list.append(operator + right.rjust(width - 1))
        # Create a line of dashes equal to the width
        line3_list.append("-" * width)

        # If answers are requested
        if show_answers:
            # Calculate the answer based on the operator
            if operator == "+":
                answer = str(int(left) + int(right))
            else:
                answer = str(int(left) - int(right))
            # Right-align the answer with the same width
            line4_list.append(answer.rjust(width))

    # Join each line with four spaces in between problems
    arranged_problems = "    ".join(line1_list) + "\n" + "    ".join(line2_list) + "\n" + "    ".join(line3_list)
    
    # If answers are requested, add the fourth line
    if show_answers == True:
        arranged_problems += "\n" + "    ".join(line4_list)

    # Return the final formatted string
    return arranged_problems


# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
