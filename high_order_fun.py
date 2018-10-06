from builtins import abs
def add(a,b,f):
    return f(a)+f(b)
print(add(-5,-9,abs))
