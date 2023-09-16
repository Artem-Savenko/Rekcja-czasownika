from src.config import allEntries

def parseCommand(command):
    command = command.split(' ')
    cmd = command[0].lower()

    if cmd == 'wylicz':
        printAll()
    elif cmd == 'wyjdź':
        quit()
    elif cmd == 'znajdź':
        find(command[1])
    elif cmd == 'usuń':
        delete(command[1])
    else:
        print('Nieznana komenda!')

def printAll():
    for e in allEntries:
        print(e.word)
    print('\n', end="")

# Finds and prints a word
def find(word):
    for entry in allEntries:
        if entry.word.lower() == word.lower():
            print(entry)
            return
    print('Takie hasło nie istnieje!')


def delete(word):
    word = word.lower()
    for i in range(len(allEntries)):
        if allEntries[i].word.lower() == word:
            allEntries.pop(i)
            return
    print('Takie hasło nie istnieje!')
