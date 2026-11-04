numbers = []
number = 1

while number <= 40:
    if (
        number == 1
        or number % 2 == 0
        and number != 2
        or number % 3 == 0
        and number != 3
        or number % 5 == 0
        and number != 5
    ):
        pass
    else:
        numbers.append(number)

    number += 1

print(numbers)
