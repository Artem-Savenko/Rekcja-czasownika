from src.case import Case

class Entry:
    def __init__(self, word, casesStr, examples):
        self.word = word
        self.cases = self.strToCases(casesStr)
        self.examples = examples

    def __repr__(self):
        result = '*' *50 + '\n'
        result += self.word + '    ' + self.cases[0].__repr__()

        # If we have multiple cases:
        if len(self.cases) > 1:
            for case in self.cases[1:]:
                result += '\n' + ' ' * (len(self.word) + 4) + case.__repr__()

        # Examples part
        result += '\n' + '-' *50
        result += '\nPrzykłady:'
        for i in range(len(self.examples)):
            result += '\n' + str(i +1) + '. ' + self.examples[i]

        return result

    def strToCases(self, str):
        if str == '':
            return [Case('')]

        list = []
        for c in str:
            list.append(Case(c))
        return list