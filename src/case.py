
class Case:
    allCases = {'M': 'Kto? Co?',                  #'Mianownik'
                'D': 'Kogo? Czego?',              #'Dopełniacz'
                'C': 'Komu? Czemu?',              #'Celownik'
                'B': 'Kogo? Co?',                 #'Biernik'
                'N': 'Z kim? Z czym?',            #'Narzędnik'
                'J': 'O kim? O czym?',            #'Miejscownik'
                'W': 'Zwrot do kogoś lub czego?'} #'Wołacz'

    def __init__(self, letter = ''):
        self.letter = ''
        if letter.upper() in self.allCases:
            self.letter = letter.upper()

    def __repr__(self):
        if self.letter == '':
            return '[]'

        return '[' + self.letter + ' - ' + Case.allCases[self.letter] + ']'

    @staticmethod
    def getValidCasesSet():
        return set(Case.allCases.keys())