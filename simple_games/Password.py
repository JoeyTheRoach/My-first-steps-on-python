import random
chars = '1234567890qwertyuioppasdfghjklzxcvbnm,[;.]/{:>>?"}<QWERTYUIOPASDFGHJKLZXCVBNM,.'
number = input('Сколько хочешь паролей? ')
length = input('Насколько длинных? ')
number = int(number)
length = int(length)
for n in range(length):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)
