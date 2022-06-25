x_or_o = ["X", "O"]
default = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
deck = default
mover = 0
x = True
breaks = "/---------WARNING!---------/"
# purpose
def run():
    global deck
    global mover
    global x
    while True:
        user_input = input(f"Place a {x_or_o[mover]}:\n-")
        int_user_input = int(user_input)
        first_culumn = int_user_input - 1
        first_culumn = first_culumn // 3
        second_culumn = int_user_input - first_culumn * 3 - 1
        if deck[first_culumn][second_culumn] not in x_or_o:
            deck[first_culumn][second_culumn] = x_or_o[mover]
            break
        else:
            print(breaks)
            print("--This segment is already filles!--")
            continue
    display = f"{deck[0][0]} | {deck[0][1]} | {deck[0][2]}\n{deck[1][0]} | {deck[1][1]} | {deck[1][2]}\n{deck[2][0]} | {deck[2][1]} | {deck[2][2]}"
    print(display)

    check_1 = deck[0][0] in x_or_o and deck[0][0] == deck[0][1] and deck[0][0] == deck[0][2]
    check_2 = deck[1][0] in x_or_o and deck[1][0] == deck[1][1] and deck[1][0] == deck[1][2]
    check_3 = deck[2][0] in x_or_o and deck[2][0] == deck[2][1] and deck[2][0] == deck[2][2]
    check_4 = deck[0][0] in x_or_o and deck[0][0] == deck[1][0] and deck[0][0] == deck[2][0]
    check_5 = deck[0][1] in x_or_o and deck[0][1] == deck[1][1] and deck[0][1] == deck[2][1]
    check_6 = deck[0][2] in x_or_o and deck[0][2] == deck[1][2] and deck[0][2] == deck[2][2]
    check_7 = deck[0][0] in x_or_o and deck[0][0] == deck[1][1] and deck[0][0] == deck[2][2]
    check_8 = deck[0][2] in x_or_o and deck[0][2] == deck[1][1] and deck[0][2] == deck[2][0]

    check = check_1 or check_2 or check_3 or check_4 or check_5 or check_6 or check_7 or check_8
    if check == True:
        print(f"\n|--{x_or_o[mover]} has won!--|")
        x = False

    if mover == 0:
        mover = 1
    else:
        mover = 0

while x:
    run()