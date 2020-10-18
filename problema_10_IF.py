g=int(input('numarul gainilor este'))
p=int(input('numarul boabelor este '))
if(p//(g+1)) and (p%(g=1)==0):
    print('numarul boabelor primite este', int(p/(g+1)), 'egalitate')
elif p/g:
    print('copan a primit mai mult cu ', p%(g+1) , 'boabe ')    