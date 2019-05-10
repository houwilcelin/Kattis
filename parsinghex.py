# -*- coding: utf-8 -*-
import re
while True:
    try:
        hexa = re.compile(r'0[xX][a-fA-F0-9]{1,8}')
        for val in hexa.findall(input()):
            print(val, int(val, 16))
    except:
        exit(0)
