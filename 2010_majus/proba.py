import math
def fizetendo(l,f):
    ut=l[2]-l[1]
    ut10=math.ceil(ut/10)
    fiz=ut10*f
    m=fiz%5
    if m>0 and m<3:
        fiz=fiz-m
    elif m>2 and m<5:
        fiz=fiz-m+5
    return fiz

print(fizetendo([0, 0, 11], 71))