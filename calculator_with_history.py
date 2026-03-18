HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as f:
            content = f.readlines()
            if len(content) == 0:
                print("No history found")
            else:
                for line in content:
                    print(line)
    except FileNotFoundError:
        print("No history found")
def clear_history():
    with open(HISTORY_FILE, 'w') as f:
        print("History was cleared")

def save_to_history(equation, result):
    lines = []
    try:
        with open (HISTORY_FILE, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        pass
    serial = len(lines) + 1
    
    with open(HISTORY_FILE, 'a') as f:
        append = f.write(f"{serial}. {equation} = {result}\n")

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Please use proper SPACING between the equation numbers or Enter a valid equation\n")
        return

    num1 = float(parts[0])
    num2 = float(parts[2])
    op = parts[1]

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    elif op == "%":
        result = num1 % num2
    else:
        print("Enter a valid equation")
        return

    if int(result) == result:
        result = int(result)

    print("Result: ", result)
    save_to_history(user_input, result)

def main():
    print("----------Welcome to Calculator----------\n")
    while True:
        user_input = input("Enter a equation (e.g: 1 + 2) or command (e.g: History, Clear, Exit): ").lower()
        if user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        elif user_input == "exit":
            print("Thanks for using Calculator... Good bye!")
            break
        else:
            calculator(user_input)
            
main()