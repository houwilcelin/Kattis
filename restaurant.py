n = int(input())
while n > 0:
    pile1, pile2 = 0, 0
    for i in range(n):
        act, c = input().split()
        c = int(c)
        if act == 'DROP':
            """if pile1 > 0:
                print(f'MOVE 1->2 {pile1}')
                pile2 += pile1
                pile1 = 0"""
            print(f'DROP 2 {c}')
            pile2 += c

        else:
            if pile1 >= c:
                print(f'TAKE 1 {c}')
                pile1 -= c
            else:
                if pile1 != 0:
                    print(f'TAKE 1 {pile1}')
                    c -= pile1
                    pile1 = 0
                print(f'MOVE 2->1 {pile2}')
                pile1 += pile2
                pile2 = 0
                print(f'TAKE 1 {c}')
                pile1 -= c
    n = int(input())
    if n > 0: print()
