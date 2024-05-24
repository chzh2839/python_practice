class Fourcal:
    # def setdate(self, first, second):
    #     self.first = first
    #     self.second = second
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = Fourcal(4,2)
# a.setdate(4,2)
print(a.sum())
print(a.sub())
print(a.mul())
print(int(a.div()))