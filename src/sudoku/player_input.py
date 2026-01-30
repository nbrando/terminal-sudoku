def player_input():
    row = int(input("Enter Row (1-9): "))
    col = int(input("Enter Column (1-9): "))
    value = int(input("Enter input value (0-9): "))

    return (row - 1, col - 1, value)
