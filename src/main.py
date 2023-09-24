from src import config
from src import entriesParser as parser
import shlex

config.init()  # init global list allEntries

print('=' * 10 + ' REKCJA CZASOWNIKA ' + '=' * 10 +
    '\nTen program jest interaktywnym słownikiem, w którym możesz przechowywać rekcje czasowników.'
	'\nAby wyświetlić wszystkie hasła, wpisz: wylicz'
	'\nAby pokazać rekcję hasła, wpisz: znajdź <hasło>'
	'\nAby wyjść z programu, wpisz: wyjdź'
	'\nAby wyświetlić listę wszystkich komend, wpisz: pomoc\n')

while (True):
    cmd = input('Wpisz komendę: ')
    parser.parseCommand(shlex.split(cmd))