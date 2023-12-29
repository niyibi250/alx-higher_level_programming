#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i < j and i != j:
            if i != 8 or j != 9:
                print("{0:}{1:}".format(i, j), end=', ')
            elif i == 8 and j == 9:
                print("{0:}{1:}".format(i, j))
        else:
            continue
