
lst_digit = []
for i in range(10, 0, -1):
    lst_digit.append(int(input(f"Введите число (осталось ввести:{i})")))
flag = "Yes"
for i in lst_digit:
    if i % 2 == 1:
        flag = "No"
        break
print(flag)
