
def welcome(x) -> str:
    x = x[12:-1]
    dynamic_message = "Welcome in <@" + x + ">!"
    return dynamic_message
