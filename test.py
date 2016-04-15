import random

vertical=1
horizontal=1

penV=-1
penH=-1

ut=0

lightOnV=True
x=1
while x<100:
    x+=1
    if lightOnV:
        ut+=penH*horizontal
        if vertical<=0:
            lightOnV=False
        else:
            vertical -=1
    else:
        
        ut+=penV*vertical
        if horizontal<=0:
            lightOnV=True
        else:
            horizontal -=1

    temp=random.random()
    if temp>0.5:
        vertical+=1
    temp=random.random()
    if temp>0.5:
        horizontal+=1
    print (ut)
    print (vertical, horizontal)
