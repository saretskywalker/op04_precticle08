n = int(input("Введите кол-во чисел в последжовательности "))
if n < 2:
    print("Введите чило большее или равное двум")
else:

    biggest = -9999999
    bigger = -999999
    for i in range(n):
        digit = int(input("Введите число"))
        if digit > biggest:
            bigger = biggest
            biggest = digit
    print(f"""Самое больше {biggest}
второе по величине {bigger}""")

