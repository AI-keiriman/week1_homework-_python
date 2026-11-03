number = 1

while number <= 40:
    if number % 3 == 0 or "3" in str(number):
        print("スパルタ！")
    else:
        print(number)

    number += 1
