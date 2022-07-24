import random
HANGMANPICS = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''','''

    +---+
    |   |
    O   |
        |
        |
        |
 =========''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
 =========''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========''','''

   +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========''','''

   +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 ========''']
words = 'муравей бабуин барсук медведь бобр верблюд кошка моллюск кобра пума койот ворона олень собака осел утка орел хорек лиса лягушка коза гусь ястреб ящерица лама моль обезьяна лось мышь мул тритон выдра сова панда попугай голубь питон кролик баран крыса носорог лосось акула змея паук аист лебедь тигр жаба форель индейка черепаха ласка кит волк вомбат зебра'.split()
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedletters, correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Неправильные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    blanks ='*'*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end='')
    print ()
def getGuess(alreadyGuessed):
    while True:
        print('Введите букву ' )
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Ваша буква:')
        elif guess in alreadyGuessed:
            print ('Эта буква уже была использована')
        elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
            print('Используйте только кириллицу')
        else:
            return guess

def playAgain():
    print('Хотите попробовать ещё раз? ("Да" или "Нет")')
    return input().lower().startswith('д')
print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters,secretWord)
    guess = getGuess(missedLetters+correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Ура! Было загадано слово "'+secretWord+'"! Вы победили!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('К сожалению, вы проиграли. После '+str(len(missedLetters))+ ' ошибок и '+str(len(correctLetters))+'угаданных букв игра окончена. Загаданное слово: "'+secretWord+'"')
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
    
            
