import pickle
import config
from entry import Entry


# Looks for the 'word' in the entire list (config.allEntries) using case-insensitive search.
# If found - returns the reference to the object, otherwise returns None.
def _findWord(word):
    word = word.lower()
    for entry in config.allEntries:
        if word == entry.word.lower():
            return entry
    return None


def addCases(word, cases):
    entry = _findWord(word)
    if entry is None:
        return

    entry.addCases(cases)


def deleteCases(word, cases):
    entry = _findWord(word)
    if entry is None:
        return

    entry.removeCases(cases)


def addExamples(word, examples):
    entry = _findWord(word)
    if entry is None:
        return

    for ex in examples:
        entry.examples.append(ex)


def removeExamples(word, exIndexes):
    entry = _findWord(word)
    if entry is None:
        return

    # convert the list to sorted integers
    indexes = set()
    for i in exIndexes:
        try:
            indexes.add(int(i) - 1)  # -1 because user provides 1-based indexes
        except ValueError:
            pass  # ignore non-ints
    indexes = list(indexes)
    indexes.sort()
    indexes.reverse()

    for i in indexes:
        if 0 <= i < len(entry.examples):
            entry.examples.pop(i)


def parseCommand(command):
    if len(command) == 0:
        return
    arg0 = command[0].lower()

    if arg0 == 'wylicz':
        printAll()
    elif arg0 == 'wyjdź':
        return
    elif arg0 == 'znajdź':
        if len(command) >= 2:
            find(command[1])
    elif arg0 == 'pomoc':
        showHelp()
    elif arg0 == 'dodaj':
        addWord(command[1], command[2] if len(command) >= 3 else '', _extractExamples(command))
    elif arg0 == 'usuń':
        if len(command) >= 2:
            delete(command[1])
    elif arg0 == 'przykład_dodaj':
        if len(command) >= 2:
            addExamples(command[1], command[2:])
    elif arg0 == 'przykład_usuń':
        if len(command) >= 2:
            removeExamples(command[1], command[2:])
    elif arg0 == 'przypadek_usuń':
        if len(command) >= 3:
            deleteCases(command[1], command[2])
    elif arg0 == 'przypadek_dodaj':
        if len(command) >= 3:
            addCases(command[1], command[2])
    elif arg0 == 'przemianuj':
        if len(command) >= 3:
            rename(command[1], command[2])
    else:
        print('Nieznana komenda!')


def printAll():
    for e in config.allEntries:
        print(e.word)
    print('\n', end="")


# Finds and prints a word and its assigned cases + examples
def find(word):
    entry = _findWord(word)
    if entry is None:
        print('Takie hasło nie istnieje!')
        return

    print(entry, end='\n\n')  # print 2 new lines for readability


def delete(word):
    word = word.lower()
    for i in range(len(config.allEntries)):
        if config.allEntries[i].word.lower() == word:
            config.allEntries.pop(i)
            return
    print('Takie hasło nie istnieje!')


def rename(oldWord, newWord):
    entry = _findWord(oldWord)
    if entry is None:
        print('Takie hasło nie istnieje!')
        return

    entry.word = newWord


def addWord(word, casesStr, examples=[]):
    config.allEntries.append(Entry(word, casesStr, examples))


def _extractExamples(command):
    if len(command) >= 3:  # indexes meaning: 0=CMD, 1=WORD, 2=CASES, 3,4,5,etc.=EXAMPLES
        return command[3:]

    return []  # no examples were provided!


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


def printWelcomeMsg():
    print('=' * 10 + ' REKCJA CZASOWNIKA ' + '=' * 10 +
          '\nTen program jest interaktywnym słownikiem, w którym możesz przechowywać rekcje czasowników.'
          '\nAby wyświetlić wszystkie hasła, wpisz: wylicz'
          '\nAby pokazać rekcję hasła, wpisz: znajdź <hasło>'
          '\nAby wyjść z programu, wpisz: wyjdź'
          '\nAby wyświetlić listę wszystkich komend, wpisz: pomoc\n')


def loadEntriesFromFile():
    try:
        config.allEntries = pickle.load(open('entries.txt', 'rb'))
    except:
        config.allEntries = list()


def saveEntriesToFile():
    pickle.dump(config.allEntries, open('entries.txt', 'wb'))
