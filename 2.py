txt = open("2.txt").read()
ltt = 'abcdefghijklmnopqrstuvwxyz'
for a in txt:
    if (a in ltt):
        print(a, end="")
