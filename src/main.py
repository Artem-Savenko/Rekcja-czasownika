import config
import entriesParser as parser
import shlex


config.init()  # init global list allEntries
parser.loadEntriesFromFile()
parser.printWelcomeMsg()

command = ''
while command != 'wyjdź':
    command = input('Wpisz komendę: ')
    parser.parseCommand(shlex.split(command))

parser.saveEntriesToFile()
