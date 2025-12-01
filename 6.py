import random
digit = random.randint(1,10)
for i in range (3, 0, -1):
    choice = int(input("Выберите число от 1 до 10 "))
    if choice == digit:
        print("Угадали!!!")
        break
    else:
        if choice > digit:
            print("""Неверно :( 
            
            
            (тс.... загаданное число меньше)
            
            
            
            """)
        else:
            print("""Неверно :( 
            
            
            
            (тс.... загаданное число больше)
            
            
            
            """)
