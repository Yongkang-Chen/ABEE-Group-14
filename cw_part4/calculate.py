import re
from math import *


# Process the expression from a string to a list, solving the problem of whether the bar is a minus or minus sign
def formula_format(formula):
    """
    :param formula: str
    """
    formula = re.sub(' ', '', formula)  # Remove the space s from the formula
    # Split by 'dashed digits', where the regular expression: (\-\d+\.? \d*) in brackets:
    formula_list = [i for i in re.split('(-[\d+,π,e]\.?\d*)', formula) if i]
    final_formula = []
    for item in formula_list:
        # The formula starts with a bar, so the first digit is negative and the bar is negative
        if len(final_formula) == 0 and re.match('-[\d+,π,e]\.?\d*$', item):
            final_formula.append(item)
            continue
        # If the current formula list [the last element is operator '+', '-', '*', '/', '(',' % ', '^'], rung as a minus sign
        if len(final_formula) > 0:
            if re.match('[\+\-\*\/\(\%\^]$', final_formula[-1]):
                final_formula.append(item)
                continue
        item_split = [i for i in re.split('([\+\-\*\/\(\)\%\^\√])', item) if i]
        final_formula += item_split
    return final_formula


# Determines whether it is an operator, and returns True if it is
def is_operator(e):
    """
    :param e: str
    :return: bool
    """
    opers = ['+', '-', '*', '/', '(', ')', '%', '^', '√', 'sin', 'arcsin', 'ln']
    return True if e in opers else False


# Compare two consecutive operators to determine whether to push or flick the stack
def decision(tail_op, now_op):
    """
    :param tail_op: the last operator on the operator stack
    :param now_op: the current operator taken form the arithmetic list
    :return: 1 represents the pop stack operation,and 0 represents the last element in the pop operator stack'('，-1 presentation stack
    """
    # Define four operator levels
    rate1 = ['+', '-']
    rate2 = ['*', '/', '%']
    rate3 = ['^', '√', 'sin', 'arcsin', 'ln']
    rate4 = ['(']
    rate5 = [')']

    if tail_op in rate1:
        if now_op in rate2 or now_op in rate3 or now_op in rate4:
            return -1
        else:
            return 1

    elif tail_op in rate2:
        if now_op in rate3 or now_op in rate4:
            return -1
        else:
            return 1

    elif tail_op in rate3:
        if now_op in rate4:
            return -1
        else:
            return 1

    elif tail_op in rate4:
        if now_op in rate5:
            return 0
        else:
            return -1



# Pass in two numbers, an operator, and return the corresponding result depending on the operator
def calculate(n1, n2, operator):
    """
    :param n1: float
    :param n2: float
    :param operator: + - * / % ^
    :return: float
    """
    result = 0
    if operator == '+':
        result = n1 + n2
    if operator == '-':
        result = n1 - n2
    if operator == '*':
        result = n1 * n2
    if operator == '/':
        result = n1 / n2
    if operator == '%':
        result = n1 % n2
    if operator == '^':
        result = n1 ** n2
    return result




# Once you've computed the result, calculate √(), sin(), or arcsin()
def Higher_order_function(op_stack, num_stack):
    if op_stack[-1] == '√':
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(sqrt(num2))
    elif op_stack[-1] == 'sin':
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(sin(num2))
    elif op_stack[-1] == 'arcsin':
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(asin(num2))
    elif op_stack[-1] == 'ln':
        op = op_stack.pop()
        num2 = num_stack.pop()
        num_stack.append(log(num2))




# Is responsible for iterating through the characters in the arithmetic list, deciding whether to push into the number stack or push into the operator stack or flick the stack
def final_calc(formula_list):
    """
    :param formula_list: arithmetic list
    :return: result
    """
    num_stack = []
    op_stack = []
    for item in formula_list:
        operator = is_operator(item)
        if not operator:
            if item == 'π':
                num_stack.append(pi)
            elif item == '-π':
                num_stack.append(-pi)
            elif item == 'e':
                num_stack.append(e)
            elif item == '-e':
                num_stack.append(-e)
            else:
                num_stack.append(float(item))
        else:
            while True:
                if len(op_stack) == 0:
                    op_stack.append(item)
                    break
                tag = decision(op_stack[-1], item)
                if tag == -1:
                    op_stack.append(item)
                    break
                elif tag == 0:
                    op_stack.pop()
                    Higher_order_function(op_stack, num_stack)
                    break
                elif tag == 1:
                    if item in ['√', 'sin', 'arcsin']:
                        op_stack.append(item)
                        break
                    op = op_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    num_stack.append(calculate(num1, num2, op))
    while len(op_stack) != 0:
        op = op_stack.pop()
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        num_stack.append(calculate(num1, num2, op))
    result = str(num_stack[0])
    if result[len(result) - 1] == '0' and result[len(result) - 2] == '.':
        result = result[0:-2]
    return result




if __name__ == '__main__':
    # formula = "2 * ( 3 - 5 * ( - 6 + 3 * 2 / 2 ) )"
    formula = "arcsin ( 0 )"
    formula_list = formula_format(formula)
    result = final_calc(formula_list)
    print("equation：", formula)
    print("result：", result)

