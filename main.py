import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():    # symbols.items gets both key(symbol) and value(symbol_count) from the dictionary ;)
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            column.append(value)
            current_symbols.remove(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 to " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter number within the range.")
        else:
            print("Please enter a number.")
    
    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? ₹")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between ₹{} - ₹{}.".format(MIN_BET, MAX_BET))
        else:
            print("Please enter a number.")
    return amount



def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if(total_bet > balance):
            print("You do not have enough currency.\nC u r r e n t  b a l a n c e :- ₹{}".format(balance))
        else:
            break

    print("You are betting ₹{} on {} lines. Total bet is equal to: ₹{}".format(bet, lines, total_bet))

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print("You won ₹{}\nYou won on line {}".format(winnings,winning_lines))
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print("Current balance is : ₹{}".format(balance))
        answer = input("Press ENTER to play or q to QUIT.")
        if answer == "q":
            break
        print("B E S T  O F  L U C K  !!!")
        balance += spin(balance)

    print("You left the game with ₹{}".format(balance))

main()
