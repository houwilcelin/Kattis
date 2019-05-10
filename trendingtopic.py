# -*- coding: utf-8 -*-
class JQ:
    def __init__(self):
        self.tab = []
        self.lc = 0

    def add(self, _nbr_text):
        if len(self.tab) > 0 and self.tab[len(self.tab)-1][0] == _nbr_text:
            self.tab[len(self.tab)-1][1] += 1
        else:
            self.tab.append([_nbr_text, 1])
        if len(self.tab) == 8:
            self.tab.pop(0)

    def last_count(self, current_step):
        c = 0
        for i in range(len(self.tab)-1, -1, -1):
            val = self.tab[i]
            if (current_step - 7) < val[0] <= current_step:
                c += val[1]
            else:
                self.lc = c
                return c
        self.lc = c
        return c

    def __repr__(self):
        return '%s' % self.tab


def print_(d, top):
    print('<top %d>' % top)
    for i in range(top):
        v = d[i]
        print(v[0], v[1].lc)
    l = d[top-1][1].lc
    if len(d) > top:
        for i in range(top, len(d)):
            v = d[i]
            if v[1].lc == l:
                print(v[0], v[1].lc)
            else:
                break
    print('</top>')


data = {}
readingText, nbr_text = False, 0
while True:
    try:
        inp = input()
        if inp == '<text>':
            readingText = True
            nbr_text += 1
        elif inp == '</text>':
            readingText = False
            # print(sorted(data))
        elif readingText:
            for word in inp.split():
                if len(word) >= 4:
                    data[word] = data.get(word, JQ())
                    data[word].add(nbr_text)
            #print('read %s from text %d'%(inp,nbr_text))
        elif inp.startswith('<top '):
            d_x = sorted(data.items(),
                         key=lambda it: (-it[1].last_count(nbr_text), it[0]))
            print_(d_x, int(inp.split()[1]))
            #print('request %s' % inp)
    except Exception as e:
        # print(e)
        break
