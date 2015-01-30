# -*- coding: ascii -*-
data = input('text: ')
re = ''
i = 0
def to2num(g):
    for x in g:
        d = ord(x)
        return bin(d)[2:].zfill(8)+'00'
a = list(range(int((len(data)*10)/6)))
def ency(g):
    hi = ''
    for j in g:
        k = int(j,2)
        t = str(k)
        tmp = get(t[len(t)-1])
        hi += '\\%'+t+tmp
    return hi        
def  get(h):
    if h == '1': return 'a'
    if h == '2': return 's'
    if h == '3': return 'd'
    if h == '4': return 'q'
    if h == '5': return 'w'
    if h == '6': return 'r'
    if h == '7': return 'b'
    if h == '8': return 'm'
    if h == '9': return 'y'
for x in data:
    re += to2num(x)
for t in range(int((len(data)*10)/6)):
    v = ''
    for j in range(6):
         v += re[i]
         i+=1
    a[t] = v     
if(len(a[len(a)-1]) != 6):
    a[len(a)-1] += '00'
print('hash: ',ency(a)+"\\")
