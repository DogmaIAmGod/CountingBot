import re


def getMath1(user_input: str) -> str:
    # new_math(user_input)
    parts = user_input.strip().split()
    parts = parts[-3:]
    returnStatement = mathing(parts[0], parts[1], parts[2])
    return f'{parts[0]} {parts[1]} {parts[2]} = {returnStatement}'


def getMath(user_input: str) -> str:
    no_space = user_input.replace(" ", "")
    no_letters = re.sub(r'[a-zA-Z]', '', no_space)
    which_first = find_order(no_letters)
    f_eq = first_equation(no_letters, which_first)
    split_equation = split_by_parts(f_eq, no_letters)
    math = perform_operations(split_equation[0], split_equation[1:])
    return f'{add_spaces_between_characters(no_letters)} = {math}'


def add_spaces_between_characters(input_string):
    result = ""
    for char in input_string:
        result += char + " "
    return result.strip()


def perform_operations(equation, operations):
    result = eval(equation)
    for op in operations:
        result = eval(str(result) + op)
    return result


def find_order(input_str: str) -> int:
    if "*" in input_str:
        return 1
    if "/" in input_str:
        return 2
    if "+" in input_str:
        return 3
    if "-" in input_str:
        return 4


def first_equation(input_str: str, which_first: int) -> str:
    if which_first == 1:
        number = input_str.find('*')
    elif which_first == 2:
        number = input_str.find('/')
    elif which_first == 3:
        number = input_str.find('+')
    else:
        number = input_str.find('-')

    return input_str[number - 1] + input_str[number] + input_str[number + 1]


def split_by_parts(target: str, whole: str):
    index = whole.find(target)
    first_part = find_number_operator_combinations(whole[:index])
    second_part = [s[::-1] for s in first_part]
    second_part.insert(0, target)
    third_part = (find_operator_and_number(whole[index + len(target):]))
    third_part = second_part + third_part
    order_operations = sort_array_except_first(third_part)
    return order_operations


def find_number_operator_combinations(expression):
    pattern = r'\d+[+\-*/]'
    matches = re.findall(pattern, expression)
    return matches


def find_operator_and_number(text):
    pattern = r'([-+*/]\d+(?:\.\d+)?)'
    matches = re.findall(pattern, text)
    return matches


def custom_sort(string):
    if string.startswith('*'):
        return 0, string
    elif string.startswith('/'):
        return 1, string
    elif string.startswith('-'):
        return 2, string
    elif string.startswith('+'):
        return 3, string
    else:
        return 4, string


def sort_array_except_first(array):
    first_item = array[0]
    rest_items = sorted(array[1:], key=custom_sort)
    rest_items.insert(0, first_item)
    return rest_items


def mathing(num1: str, opp: str, num2: str) -> str:
    number1: float = float(num1)
    number2: float = float(num2)
    if opp == '+' or opp == 'plus':
        return str(number1 + number2)
    if opp == '-' or opp == 'subtract':
        return str(number1 - number2)
    if opp == '*' or opp == 'times':
        return str(number1 * number2)
    if opp == '/' or opp == 'divide':
        if number2 == 0:
            return "DIVIDE BY ZERO ERROR"
        return str(number1 / number2)
