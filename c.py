name = input("氏名を入力して下さい:")
name_count = 0
for word in name:
    if word.isalpha():
        name_count += 1
print(name_count)
