#generator
def generator(x,y):
    if x > y:
        return None
    g = (i for i in list(range(x,y)))
    return g
g = generator(1,20)
if g is not None:
    for n in g:
        print(n)
#fibernacii
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fibernacii(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n+=1
    return "Done"
g = fibernacii(50)
for i in g:
    print(i)
