a=int(input('prima nota este'))
b=int(input('a doua nota este'))
c=int(input('a treia nota este'))
if (c>=8):
    print(a,b,c)
if (c<8):
    if (a>b):
        print(a)
    if (b<a):
        print(b)
    if (b==a):
        print(a) or (b)
