#使用切片实现去掉字符串首尾+
ss='+ssdfjasdfkjasd sd;fsda+'
def trim(s):
    if s[0]=='+':
        s=s[1:]
    if s[-1:]=='+':
        s=s[:-2]
    return s
print(trim(ss))
