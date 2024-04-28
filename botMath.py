import re


def getMath(user_input: str) -> str:
    print(user_input)
    no_trigger = user_input.replace("FindTheWord what is ", "")
    no_space = no_trigger.replace(" ", "")
    return f'{add_spaces_between_characters(no_space)} = {eval(no_space)}'


def add_spaces_between_characters(input_string):
    pattern = r'([-+*/])'
    result = re.sub(pattern, r' \1 ', input_string)
    return result
