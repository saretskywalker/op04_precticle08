flag = "Yes"
for i in range(10,0,-1):
    digit = int(input(f"Введите число (осталось ввести:{i})"))
    if digit % 2 == 1:
        flag = "No"
        break
print(flag)
