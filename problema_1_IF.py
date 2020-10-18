n1=int(input('numarul primului elev este '))
n2=int(input('numarul elevului doi este'))
n3=int(input('numarul elevului trei este '))
p1=int(input('punctajul primului elev este'))
p2=int(input('punctajul elevului doi este'))
p3=int(input('punctalui elevului trei este'))
if (p1>p2) and (p1>p3) :
    print('punctajul maximal il are elevul', n1)
if (p2>p1) and (p2>p3) :
    print('punctajul maximal il are elevul', n2)
if (p3>p1) and (p3>p2) :
    print('punctajul maximal il are elevul', n3)
if (p1==p2) and (p1>p3) and (p2>p3) :
    print('punctajul maximal il au elevii', n1 and n2)
if (p2==p3) and (p2>p1) and (p3>p1) :
    print('punctajul maximal il au elevii', n2 and n3)
if (p1==p3) and (p1>p2) and (p3>p2) :
    print('punctajul maximal il au elevii', n1 and n3)



