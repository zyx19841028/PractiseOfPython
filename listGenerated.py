import os
#list generate expression
def generateList(x,y):
    if x <= y:
        l = list(range(x,y))
    else:
        l=[]
    return l
print(generateList(1,23))
print(generateList(1,1))
print(generateList(11,1))
#another expression
def generateList2(x,y):
    if x < y:
        l=[i * i for i in list(range(x,y))]
    else:
        l=[]
    return l
print(generateList2(1,5))
#another generated expression
def generateList3(x,y):
    if x < y:
        t=[i*i for i in list(range(x,y)) if i % 2 == 0]
    else:
        t=[]
    return t
print(generateList3(1,50))
#two loops to generate expressions 
def generateList4(str1,str2):
    l=[x+y for x in str1 for y in str2]
    return l
print(generateList4('ABCD','EFG'))
#for dict
def generateList4(d):
    l=[]
    if not isinstance(d,dict):
        return []
    l=[str(k)+"="+str(v) for k,v in d.items()]
    return l

print(generateList4({"this":0,"is":1,"a":2,"test":3}))
#practise
L1 = ['Hello', 'World', 18, 'Apple', None]
def tolower(s):
    l = [x.lower() for x in s if isinstance(x,str)]
    return l
print(tolower(L1))
