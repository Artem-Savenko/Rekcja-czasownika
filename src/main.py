import config
import entriesParser as parser
import pickle
import shlex

config.init()  # init global list allEntries

try:
    config.allEntries = pickle.load(open('entries.txt', 'rb'))
except:
    config.allEntries = list()

print('=' * 10 + ' REKCJA CZASOWNIKA ' + '=' * 10 +
      '\nTen program jest interaktywnym słownikiem, w którym możesz przechowywać rekcje czasowników.'
      '\nAby wyświetlić wszystkie hasła, wpisz: wylicz'
      '\nAby pokazać rekcję hasła, wpisz: znajdź <hasło>'
      '\nAby wyjść z programu, wpisz: wyjdź'
      '\nAby wyświetlić listę wszystkich komend, wpisz: pomoc\n')

while (True):
    cmd = input('Wpisz komendę: ')
    parser.parseCommand(shlex.split(cmd))
