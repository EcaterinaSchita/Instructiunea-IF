a=int(input('valoarea primui numar este'))
b=int(input('valoarea numarului doi este'))
c=int(input('valoarea numarului trei este'))
if (a<b+c) and (b<c+a) and (c<a+b):
    print('Da')
else:
    print('Nu')    
