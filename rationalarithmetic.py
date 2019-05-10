gcd = lambda a, b: a if b == 0 else gcd(b, a % b)


class F:
    def __init__(self, n, d):
        self.numerator, self.denominator = n, d

    def mul(self, n):
        self.numerator *= n
        self.denominator *= n

    def arrange(self):
        pgcd = gcd(self.numerator, self.denominator)
        self.numerator //= pgcd
        self.denominator //= pgcd
        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1
        return self

    def __repr__(self):
        return "%d / %d" % (self.numerator, self.denominator)


def arrange(a: F, b: F):
    ppcm = (a.denominator * b.denominator) // gcd(a.denominator, b.denominator)
    a.mul(ppcm // a.denominator)
    b.mul(ppcm // b.denominator)


def plus(a: F, b: F) -> F:
    arrange(a, b)
    return F(a.numerator + b.numerator, a.denominator)


def minus(a: F, b: F) -> F:
    arrange(a, b)
    return F(a.numerator - b.numerator, a.denominator)


def mul(a: F, b: F):
    return F(a.numerator * b.numerator, a.denominator * b.denominator)


def div(a: F, b: F):
    return F(a.numerator * b.denominator, a.denominator * b.numerator)


def doOp(a: F, b: F, op: str) -> F:
    if op == '+':
        return plus(a, b)
    elif op == '-':
        return minus(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return div(a, b)


# print(plus(F(2, 3), F(1, 3)))
# print(F(-1, -3).arrange())
n = int(input())
for i in range(n):
    x1, y1, op, x2, y2 = input().split()
    print(doOp(F(int(x1), int(y1)).arrange(), F(int(x2), int(y2)).arrange(), op).arrange())
