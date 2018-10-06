from functools import reduce
def fn(x,y):
    return x*10 + y
def char2int(s):
    digits={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
    return digits[s]
res=reduce(fn,map(char2int,'384283'))
print(res)
