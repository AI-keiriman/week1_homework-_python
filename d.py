birthday = input("生年月日（西暦/月/日）を入力して下さい:")
list = birthday.split("/")

year = list[0]
month = list[1]
day = list[2]
print(int(year) + int(month) + int(day))
