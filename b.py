name = input("氏名を入力して下さい:")

name_count = 0
for word in name:
    if word.isalpha():
        name_count += 1

birthday = input("生年月日（西暦/月/日）を入力して下さい:")

list = birthday.split("/")

year = list[0]
month = list[1]
day = list[2]

total = name_count + int(year) + int(month) + int(day)

if total % 6 == 0:
    print("大吉")

elif total % 3 == 0:
    print("中吉")

elif total % 2 == 0:
    print("吉")

else:
    print("凶")
