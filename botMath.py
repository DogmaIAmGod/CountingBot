def getMath(user_input: str) -> str:
    parts = user_input.strip().split()
    parts = parts[-3:]
    returnStatement = mathing(parts[0], parts[1], parts[2])
    return f'{parts[0]} {parts[1]} {parts[2]} = {returnStatement}'


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
