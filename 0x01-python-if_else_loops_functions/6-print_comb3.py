#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        for k in range(1,10):
            if i<j and i!=j:
                print("{0:}{1:}".format(i,j), end=', ')
            else:
                continue
print("\n")
