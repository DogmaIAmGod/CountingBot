import pandas as pd
import time


async def quizOutput(user_message, message) -> None:
    required_df = pd.read_excel('vocab.xlsx', skiprows=0, usecols=[0, 1, 2])
    df_list = required_df.values.tolist()
    unit_list = []
    number_list = []
    send_message = ""
    dynamic_message = ""
    number = int(user_message[7:])
    print("here")
    for x in df_list:
        if x[0] not in number_list:
            number_list.append(x[0])
    if number not in number_list:
        await message.channel.send("This isn't a unit")
    else:
        for sublist in df_list:
            if sublist[0] == number:
                unit_list.append([sublist[1], sublist[2]])
        for item in unit_list:
            dynamic_message = item[1] + ' : ||' + item[0] + '||\n'
            dyn_len = len(dynamic_message)
            if dyn_len + len(send_message) < 2000:
                send_message += dynamic_message + '\n'
            else:
                await message.channel.send(send_message)
                time.sleep(.5)
                send_message = ""

        if send_message != "":
            await message.channel.send(send_message)