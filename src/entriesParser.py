from src.case import Case
from src.config import allEntries
from src.entry import Entry


def parseCommand(command):
    if len(command) == 0:
        return
    cmd = command[0].lower()

    if cmd == 'wylicz':
        printAll()
    elif cmd == 'wyjdź':
        quit()
    elif cmd == 'znajdź':
        if len(command) >= 2:
            find(command[1])
    elif cmd == 'dodaj':
        addWord(command[1], command[2], extractExamples(command))
    elif cmd == 'usuń':
        if len(command) >= 2:
            delete(command[1])
    elif cmd == 'przemianuj':
        if len(command) >= 3:
            rename(command[1], command[2])
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
            print(entry, end='\n\n') # print 2 new lines for readability
            return
    print('Takie hasło nie istnieje!')


def delete(word):
    word = word.lower()
    for i in range(len(allEntries)):
        if allEntries[i].word.lower() == word:
            allEntries.pop(i)
            return
    print('Takie hasło nie istnieje!')


def rename(oldWord, newWord):
    oldWord = oldWord.lower()
    for i in range(len(allEntries)):
        if allEntries[i].word.lower() == oldWord:
            allEntries[i].word = newWord
            return
    print('Takie hasło nie istnieje!')

def addWord(word, casesStr, examples = []):
    allEntries.append(Entry(word, casesStr, examples))


def extractExamples(command):
    if len(command) >= 3:   # 0 = dodaj, 1 = policzyć, 2 = bj, 3 = Policzę ilość przypadków
        return command[3:]

    return [] # no examples were provided!
