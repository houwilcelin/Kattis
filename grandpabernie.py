class Stack:
    def __init__(self):
        self.db = []
        self.sort = False

    def add(self, element):
        self.db.append(element)
        return self

    def get(self, idx):
        if not self.sort:
            self.db.sort()
            self.sort = True
        return self.db[idx]

    def __repr__(self):
        return ('%s' % self.db)


if __name__ == '__main__':
    db = {}
    n = int(input())
    for i in range(n):
        c, y = tuple(input().split(" "))
        db[c] = db.get(c, Stack()).add(int(y))
    n = int(input())
    for i in range(n):
        c, k = tuple(input().split(" "))
        print(db[c].get(int(k) - 1))
