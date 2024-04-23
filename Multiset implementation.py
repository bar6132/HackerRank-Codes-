class Multiset(object):
    def __init__(self):
        self.data = {}

    def add(self, val):
        if val not in self.data:
            self.data[val] = 1
        else:
            self.data[val] += 1

    def remove(self, val):
        if val in self.data and self.data[val] > 0:
            self.data[val] -= 1

    def __contains__(self, val):
        return val in self.data and self.data[val] > 0

    def __len__(self):
        return sum(self.data.values())
