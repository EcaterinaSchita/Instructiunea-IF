zn=int(input('ziua nasterii este '))
zc=int(input('ziua curenta este'))
ln=int(input('luna nasterii este'))
lc=int(input('luna curenta este'))
an=int(input('anul nasterii este '))
ac=int(input('anul curent este'))
if (lc>ln):
    print(ac-an)
if (lc=ln) and (zn>zc):
    print(ac-an)
if (zc>zn) and (lc=ln):
    print(ac-an)
if (ln<lc) and (zn=zc):
    print((ac-an)+lc)
if (ln<lc) and (zn<zc) :
    print((ac-an)+zc)
    
     