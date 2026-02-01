def player_input():
    row = get_int("Enter Row (1-9):\n> ", 1, 9)
    col = get_int("Enter Column (1-9):\n> ", 1, 9)
    value = get_int("Enter cell value (0-9):\n> ", 0, 9)

    return (row - 1, col - 1, value)


def get_int(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if not (min_value <= value <= max_value):
                raise ValueError
            return value

        except ValueError:
            print(f"> Invalid input. Value must be between {min_value} and {max_value}")
