from src.case import Case

class Entry:
    # Class Entry is a class that represents a single word with cases and examples assigned to it.
    # Attribute 'word' is simply a string, that represents the entry
    # Attribute 'cases' is a set of upper-case letters (it can be empty too) that represents the cases
    # assigned to this entry. DO NOT use this attribute directly! Use addCases() or removeCases() instead.
    # Attribute 'examples' is a list of strings where each string is an example
    def __init__(self, word, casesStr, examples):
        self.word = word
        self.examples = examples

        self.cases = set()
        self.addCases(casesStr)

    def __repr__(self):
        result = '*' *50 + '\n'
        result += self.getWordAndCasesStr()

        # Examples part
        result += '\n' + '-' *50
        result += '\nPrzykłady:'
        for i in range(len(self.examples)):
            result += '\n' + str(i +1) + '. ' + self.examples[i]

        return result

    def addCases(self, casesStr):
        for letter in casesStr:
            self.cases.add(letter.upper())
        self.cases = self.cases.intersection(Case.getValidCasesSet())

    def removeCases(self, casesStr):
        for case in casesStr:
            self.cases.discard(case.upper())

    def getWordAndCasesStr(self):
        cases = tuple(self.cases) # convert to a tuple, so we can iterate by indices
        result = ''
        result += self.word + '    '
        if len(cases) >= 1:
            result += Case(cases[0]).__repr__()
        else:
            result += '[]'

        # If we have multiple cases:
        if len(cases) > 1:
            for case in cases[1:]:
                result += '\n' + ' ' * (len(self.word) + 4) + Case(case).__repr__()

        return result
