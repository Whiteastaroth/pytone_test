#Приветсвие

print("-------------------")
print("  Добро пожаловать  ")
print("      в игру       ")
print("  крестики-нолики  ")
print("-------------------")
print("формат ввода: X и Y ")
print(" X - номер строки  ")
print(" Y - номер столбца ")

#Игровое поле

def show_field(f):

    num ='  0 1 2'
    print(num)
    for row,i in zip(f,num.split()):
        print (f"{i} {' '.join(str(j) for j in row)}")

# Проверка данных
def users_input(f,user):

    while True:
        place=input(f"Ходит {user} .Введите координаты:").split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y

# победные команды

def win_position(f, sumbols):

    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        sumbols = []
        for c in cord:
            sumbols.append(f[c[0]][c[1]])
        if sumbols == ["X", "X", "X"]:
            print("Победитель  X!!!")
            return True
        if sumbols == ["0", "0", "0"]:
            print("Победитель 0!!!")
            return True
    return False

# Показать последний ход при выигрыше и победа

def start(field):

    count=0
    while True:
        show_field(field)
        if count%2==0:
            user='X'
        else:
            user = '0'
        if count<9:
            x, y = users_input(field,user)
            field[x][y] = user

        elif count==9:
            print ('Ничья')
            break
        if win_position(field,user):
            print(f"Выйграл {user}")
            show_field(field)
            break
        count+=1

#Запуск кода
field = [['-'] * 3 for _ in range(3)]

start(field)