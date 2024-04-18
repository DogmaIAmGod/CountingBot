def display_leaderboard(user_input: str) -> str:
    if user_input == '++leaderboard':
        return create_leaderboard_message()


def create_leaderboard_message() -> str:
    with open("output.txt", 'r') as file:
        lines = file.readlines()

    data = [(line.strip().split()[0], int(line.strip().split()[1]), int(line.strip().split()[2])) for line in lines]
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    return_words: str = '--------Sorries leaderboard--------\n'
    count: int = 0

    for name, number, userid in sorted_data[:10]:
        count += 1
        return_words += f"#{count}: <@{userid}> with {number} sorries\n"
    return return_words
