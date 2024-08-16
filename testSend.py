import time

with open('array.txt', 'r') as file:
    array = [line.strip() for line in file]


async def test_send(message) -> None:
    time.sleep(2)
    for item in array:
        dynamic_message = '<@235148962103951360> doThing <@' + item + '>\n'
        await message.channel.send(dynamic_message)
        time.sleep(.5)
