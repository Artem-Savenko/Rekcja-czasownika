from src.case import Case

class Entry:
    def __init__(self, word, casesStr, examples):
        self.word = word
        self.addCases(casesStr)
        self.examples = examples

    def __repr__(self):
        result = '*' *50 + '\n'
        cases = tuple(self.cases)
        result += self.word + '    ' + cases[0].__repr__()

        # If we have multiple cases:
        if len(cases) > 1:
            for case in cases[1:]:
                result += '\n' + ' ' * (len(self.word) + 4) + case.__repr__()

        # Examples part
        result += '\n' + '-' *50
        result += '\nPrzykłady:'
        for i in range(len(self.examples)):
            result += '\n' + str(i +1) + '. ' + self.examples[i]

        return result

    def addCases(self, casesStr):
        # after converting cases, remove duplicates!
        self.cases = set(self.strToCases(casesStr))

    def strToCases(self, str):
        if str == '':
            return [Case('')]

        list = []
        valids = Case.extractValidCasesFromStr(str)
        for c in valids:
            list.append(Case(c))
        return list