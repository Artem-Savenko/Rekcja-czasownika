from src.config import allEntries
from src import entry
from src import entriesParser as parser

allEntries.append(entry.Entry('Myśleć', 'djn', ['Lubię swego kota', 'Może pomyślę nad tym...']))

while (True):
    cmd = input('Wpisz komendę: ')
    parser.parseCommand(cmd)