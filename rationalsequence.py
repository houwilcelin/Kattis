import sys
sys.setrecursionlimit(50000)


class Number:
    def __init__(self, p, q):
        self.p, self.q = p, q

    def left(self):
        return Number(self.p, self.p+self.q)

    def right(self):
        return Number(self.p+self.q, self.q)

    def parent(self):
        p_p, p_q = None, None
        if self.p > self.q:
            p_p, p_q = self.p-self.q, self.q
        elif self.p < self.q:
            p_p, p_q = self.p, self.q-self.p
        return Number(p_p, p_q)
    
    def inverse(self):
        return Number(self.q,self.p)
    

    def tuple_(self):
        return self.p, self.q

    def __repr__(self):
        return '%d/%d' % (self.p, self.q)

    @staticmethod
    def from_(inp):
        p, q = map(int, inp.split('/'))
        return Number(p, q)


def next_(number):
    if number.q == 1:
        return (number.inverse().left())
    elif number.p < number.q:
        #print('right', number.parent())
        return number.parent().right()
    else:
        return next_(number.parent()).left()
        memo = next_db.get(number.tuple_(), None)
        if memo == None:
            nl = next_(number.parent())
            #print('next_left', number.parent(), nl)
            next_db[number.tuple_()] = nl.left()
            return nl.left()
        else:
            #print('yet', number)
            return memo


next_db = {}
#fringe = [Number(1, 1)]
"""ui = next_(Number.from_('2147483/1'))
print(ui)
"""
"""while len(fringe) > 0:
    n = fringe.pop()
    print(n)
    if n.q < 3*10**6 and n.p < 3*10**6:
        fringe.extend([n.left(),n.right()])
    else:
        print(n)
        break"""
for _ in range(int(input())):
    k, inp = input().split()
    print(k, next_(Number.from_(inp)))
