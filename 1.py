## substitui todos os caracteres por dois caracteres acima, se estiver entre A e Z
txt = open("1.txt").read()
for x in txt:
    print(chr(ord(x) if ord(x)+2 < ord('a') else  ord(x)+2 if ord(x)+2 < ord('z') else ord(x)-24), end="")