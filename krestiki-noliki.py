# Выводим приветствие на экран
def hello():
    print("Добро пожаловать")
    print("     в игру     ")
    print("крестики-нолики!")

hello()

# Создаем игровое поле
pole = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
# Выводим поле в терминал
def igra():
    print(f"  0 1 2")
    print(f"0 {pole[0][0]} {pole[0][1]} {pole[0][2]}")
    print(f"1 {pole[1][0]} {pole[1][1]} {pole[1][2]}")
    print(f"2 {pole[2][0]} {pole[2][1]} {pole[2][2]}")


igra()

def pol():
    while True:
        coordinat = input("Ваш ход").split()


        if len(coordinat) != 2:
            print("Введите 2 координаты!")
            continue

        x, y = coordinat

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2 :
            print("Координаты вне диапазона")
            continue

        if pole[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y

#pol()

# Создаем победные линии

def winner():
    coord = [((0, 0), (0, 1), (0, 2)),((1, 0), (1, 1), (1, 2)),((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),((0, 0), (1, 1), (2, 2)),((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 2)),((0, 2), (1, 2), (2, 2))]

    for cord in coord:
        vvod = []
        for c in cord:
            vvod.append(pole[c[0]][c[1]])
        if vvod == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if vvod == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False

# Процесс игры
num1 = 0
while True:
    num1 += 1

    igra()

    if num1 % 2 == 1:
        print(" Ходит крестик")
    else:
        print(" Ходит нолик")
    x, y = pol()

    if num1 % 2 == 1:
        pole[x][y] = "X"
    else:
        pole[x][y] = "0"

    if winner():
        break

    if num1 == 9:
        print("Ничья")
        break


winner()