import random
c = 1
b = 0
f = 0
love = ['1','2','3','4','5','6','7','8','9','10']
while f<10:
    c = 1
    f = f + 1
    a = random.choice(love)
    while a != b:
        b = input('Угадаешь число? Попытка № ' + str(c) + ' ')
        if b != a:
            c = c + 1
            print('Не получилось, давай снова')
        elif b == a:
            print('УРАААА! Ты угадал за ' + str(c) + ' попыток!')
