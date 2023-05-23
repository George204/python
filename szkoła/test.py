def find_biggest_number(numbers):
    biggest_number = numbers[0]
    for number in numbers:
        if number > biggest_number:
            biggest_number = number
    return biggest_number

def generat_random_numbers(n):
    import random
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1, 100))
    return numbers

def move_coursor_in_terminal_to_xy(x, y):
    print(f'\033[{y};{x}H')

def replace_current_terminal_line_with_spaces(n):
    #move crursor to start of the currnent line
    
    print(' ' * n)

def wait_for_anykey():
    input('Press any key to continue...')
    
def main():
    move_coursor_in_terminal_to_xy(10, 10)
    numbers = generat_random_numbers(10)
    print(numbers)
    biggest_number = find_biggest_number(numbers)
    print(f'The biggest number is {biggest_number}')
    wait_for_anykey()
    remove_current_line_in_terminal()
    input("any key to continue")
if __name__ == '__main__':
    main()