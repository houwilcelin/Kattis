if __name__ == '__main__':

    inp, out = input(), []
    for i in inp:
        if i == "<":
            out.pop()
        else:
            out.append(i)
    print("".join(out))
