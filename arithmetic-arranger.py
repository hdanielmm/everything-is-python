import re

def arithmetic_arranger(problems: list, solve: bool = False):
    if(len(problems) > 5):
        return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""

    for problem in problems:
        if(re.search("[^\s0-9.+-]", problem)):
            if(re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'." 
            return "Error: Numbers must only contain digits."

        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        if(len(first_number) >= 5 or len(second_number) >= 5):
            return "Error: Numbers cannot be more than four digits."

        sum = ""

        if operator == "+":
            sum = str(int(first_number) + int(second_number))
        elif operator == "-":
            sum = str(int(first_number) - int(second_number))

        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = "-" * length
        res = str(sum).rjust(length)

        if problem != problems[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += line + "    "
            sumx += res + "    "
        else:
            first += top
            second += bottom
            lines += line
            sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
