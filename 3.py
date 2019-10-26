txt = open("3.txt").read()
for i,letra in enumerate(txt):
    if(
    (txt[i-3]+txt[i-2]+txt[i-1]).isupper() 
    and (txt[i+1]+txt[i+2]+txt[i+3]).isupper()  
    and ((txt[i+1]+txt[i+2]+txt[i+3]) == (txt[i-3]+txt[i-2]+txt[i-1]))
    and letra.islower()):
        print(letra,end="")
    