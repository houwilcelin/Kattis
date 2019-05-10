def getSum(b_tree, index):
    s = 0
    index += 1
    while index > 0:
        s += b_tree[index]
        # print((s, index))
        index -= index & (-index)
    return s


def update(b_tree, index, val):
    index += 1
    while index < len(b_tree):
        b_tree[index] += val
        index += index & (-index)


if __name__ == '__main__':
    n, k = tuple(map(int, (input().split(" "))))
    arr = [0] * n
    b_tree = [0] * (n + 1)
    for i in range(k):
        r = input().split(" ")
        if r[0] == 'F':
            f = int(r[1]) - 1
            old_value = arr[f]
            arr[f] ^= 1
            update(b_tree, f, arr[f] - old_value)
        else:
            l, r = int(r[1]) - 1, int(r[2]) - 1
            r_sum = getSum(b_tree, r)
            if l > 0:
                r_sum -= getSum(b_tree, l - 1)
            print(r_sum)
