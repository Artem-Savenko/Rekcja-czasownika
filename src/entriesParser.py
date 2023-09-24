from src import config
from src.entry import Entry


def findWord(word):
    word = word.lower()
    for entry in config.allEntries:
        if word == entry.word.lower():
            return entry
    return None

def addCases(word, cases):
    entry = findWord(word)
    if entry is None:
        return

    entry.addCases(cases)


def deleteCases(word, cases):
    entry = findWord(word)
    if entry is None:
        return

    entry.removeCases(cases)


def addExamples(word, examples):
    entry = findWord(word)
    if entry is None:
        return

    for ex in examples:
        entry.examples.append(ex)

def removeExamples(word, exIndexes):
    entry = findWord(word)
    if entry is None:
        return

    # convert the list to sorted integers
    indexes = set()
    for i in exIndexes:
        try:
            indexes.add(int(i) -1)   #-1 because user provides 1-based indexes
        except ValueError:
            pass    # ignore non-ints
    indexes = list(indexes)
    indexes.sort()
    indexes.reverse()

    for i in indexes:
        if 0 <= i < len(entry.examples):
            entry.examples.pop(i)

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
    elif cmd == 'pomoc':
        showHelp()
    elif cmd == 'dodaj':
        addWord(command[1], command[2] if len(command) >= 3 else '', _extractExamples(command))
    elif cmd == 'usuń':
        if len(command) >= 2:
            delete(command[1])
    elif cmd == 'przykład_dodaj':
        if len(command) >= 2:
            addExamples(command[1], command[2:])
    elif cmd == 'przykład_usuń':
        if len(command) >= 2:
            removeExamples(command[1], command[2:])
    elif cmd == 'przypadek_usuń':
        if len(command) >= 2:
            deleteCases(command[1], command[2])
    elif cmd == 'przypadek_dodaj':
        if len(command) >= 3:
            addCases(command[1], command[2])
    elif cmd == 'przemianuj':
        if len(command) >= 3:
            rename(command[1], command[2])
    else:
        print('Nieznana komenda!')

def printAll():
    for e in config.allEntries:
        print(e.word)
    print('\n', end="")

# Finds and prints a word
def find(word):
    for entry in config.allEntries:
        if entry.word.lower() == word.lower():
            print(entry, end='\n\n') # print 2 new lines for readability
            return
    print('Takie hasło nie istnieje!')


def delete(word):
    word = word.lower()
    for i in range(len(config.allEntries)):
        if config.allEntries[i].word.lower() == word:
            config.allEntries.pop(i)
            return
    print('Takie hasło nie istnieje!')


def rename(oldWord, newWord):
    oldWord = oldWord.lower()
    for i in range(len(config.allEntries)):
        if config.allEntries[i].word.lower() == oldWord:
            config.allEntries[i].word = newWord
            return
    print('Takie hasło nie istnieje!')

def addWord(word, casesStr, examples = []):
    config.allEntries.append(Entry(word, casesStr, examples))


def _extractExamples(command):
    if len(command) >= 3:   # 0 = dodaj, 1 = policzyć, 2 = bj, 3 = Policzę ilość przypadków
        return command[3:]

    return [] # no examples were provided!


def showHelp():
    print('Lista wszystkich komend:'
          '\n\twylicz - wyświetla listę wszystkich haseł w słowniku'
          '\n\tdodaj <hasło> [przypadki] [przykład1] [przykład2] [i t.d.] - dodaje nowe hasło do słownika'
          '\n\tusuń <hasło> - usuwa hasło z słownika'
          '\n\tznajdź <hasło> - wyświetla rekcje czasownika dla hasła wraz z przykładami'
          '\n\tprzemianuj <hasło> <nowe_hasło> - zmienia nazwę hasła na nową'
          '\n\tpomoc - wyświetla instrukcje co do użycia wszystkich komend tego programu'
          '\n\tprzypadek_dodaj <hasło> <przypadki> - dodaje kolejny przypadek(ki) do hasła'
          '\n\tprzypadek_usuń <hasło> <przypadki> - usuwa przypadek(ki) z hasła'
          '\n\tprzykład_dodaj <hasło> <przykład1> [przykład2] [...] - dodaje przykład(y) do hasła'
          '\n\tprzykład_usuń <hasło> <numer_przykładu 1> [numer_przykładu 2] [...] - usuwa przykład(y) z hasła; numer_przykładu jest wyświetlany'
          ' przy użyciu komendy \'znajdź <hasło>\'')
