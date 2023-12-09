def print_digit(number):
    if number == 0:
        print(0)
        return
    
    while number != 0:
        digit = number % 10
        print(digit)
        number //= 10


print_digit(100)