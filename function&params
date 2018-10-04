#!/usr/bin/python
# -*- coding: utf-8 -*-
#默认参数
def fun1(a,b,c,d=10,e=20):
    print(a,b,c,d,e)
fun1(1,2,3,15)
fun1(1,2,3)
fun1(1,2,3,e=18)
#if default parameters is a list
def fun2(L=[]):
    L.append('x')
    return L
print(fun2())
print(fun2())
#correct implementation
def fun3(L=None):
    if L is None:
        L=[]
    L.append('x')
    return L
print(fun3())
print(fun3())
#alterable parameters
def func4(*numbers):
    s=0
    print(len(numbers))
    if len(numbers) > 0:
        for i in numbers:
            s += i*i
    return s
print(func4(1,2,3,4,5,6))
l=[1,2,3,4,5,6,7]
print(func4(*l))
#key word parameters
def func5(name, age,**kv):
    print("name",name,"age",age,"others",kv)
func5("Joe",33,job='Programmer',Gender='male')
d={"Job":"Programmer","Gender":"male"}
func5("kk","dd",**d)
#named key word parameters,city and gender are named key word parameters
def func6(name,age,*params,city,gender):
    print("name",name,"age",age,"city",city,"gender",gender,"other",params)
l=[1,3,5,7,9]
func6("Joe",33,l,city='Manila',gender='male')
# a complex application
# 声明顺序必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def func7(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
func7(1, 2, 3, 'a', 'b')
func7(5,6,7)
func7(*l)
func7(3,"aa",**d)
