#iterator
l=list(range(10))
def iter(l):
    for v in l:
        print(v)
iter(l)
#
d={"name":"John","age":33,"gender":"male"}
def iter2(d):
    for k,v in d.items():
        print(k,v)
    for v in d.values():
        print(v)
    for k in d:
        print(k)
iter2(d)
#
s="abcdefghijklmnopqrstuvwxyz"
def iter3(s):
    for v in s:
        print(v)
iter3(s)
#
def maxmin(l):
    min=l[0]
    max=l[0]
    for v in l:
        if v > max:
            max = v
        if v < min:
            min = v
    return min,max
print(maxmin(l))
