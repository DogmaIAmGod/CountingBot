import re
import unicodedata
import time
from unidecode import unidecode


def get_response(user_input: str, username: str, userid: int) -> str:
    lowered: str = user_input.lower()
    replace_single(lowered)
    lowered = unidecode(lowered)
    ret = unicodedata.normalize('NFKC', lowered).encode('ascii', 'ignore')
    lowered = ret.decode("utf8")
    lowered = lowered.lower()
    lowered = replace_repeated_letters(lowered)

    if find_sorry(lowered):
        record_sorry(user_input, username)
        write_to_file(username, userid)
        returnString: str = (username + ' SAID SORRY')
        return returnString


def find_sorry(string):
    pattern = re.compile(r'sorry'
                         r'|apolog'
                         r'|sorries|'
                         r'srry|'
                         r'sowwy')
    matches = pattern.search(string)
    return matches


def replace_repeated_letters(string):
    string = re.sub(r'(.)\1+', r'\1\1', string)
    string = re.sub(r'o+', 'o', string)
    string = re.sub(r'[^a-z]', '', string)
    return string


def replace_single(string):
    string = string.replace(" ", "")
    string = string.replace("0", "o")
    string = string.replace("$", "s")
    string = string.replace("!", "i")
    string = string.replace("1", "i")
    return string


def write_to_file(content, userid):
    with open("output.txt", 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        found = False
        for line in lines:
            parts = line.strip().split()
            if parts[0] == content:
                found = True
                parts[1] = str(int(parts[1]) + 1)
                parts[2] = str(int(userid))
                file.write(' '.join(parts) + '\n')
            else:
                file.write(line)
        if not found:
            file.write(content + " 1 " + str(userid) + "\n")
        file.truncate()


def record_sorry(content, username):
    with open("sorries.txt", 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        lines.append(' '.join([time.asctime() + ' -', username + ":", '"' + content + '"']) + '\n')

        for line in lines:
            file.write(line)
        file.truncate()
