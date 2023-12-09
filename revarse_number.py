def number_revarse(number):
    if number == 0:
        print(0)
        return 0
    
    reverse = 0
    while number > 0:
        last_digit = number % 10
        reverse = (reverse * 10) + last_digit
        number //= 10
    return reverse


print(number_revarse(179))