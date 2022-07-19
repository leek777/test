'''
1.1 将序列分解为单独的变量
'''
p = (4,5)
x,y = p
# print(x,y)

data = ["leek",25,170,(1997,5,28)]
name,age,high,date = data
# print(name,age,high,date)
name,age,high,(year,mon,day) = data
# print(year,mon,day)

s = "Hello"
a,b,c,d,e = s
# print(a,b,c,d,e)
_,a,b,c,_ = s #丢弃不需要的值
#print(a,b,c)

'''
1.2 从任意长度的可迭代对象中分解元素
''' 
# *表达式的使用
import numpy as np
def drop_first_last(grades):
    first,*middle,last = grades
    return np.mean(middle)

record = ("leek","xx@qq.com","0745-1255","0745-3688")
name,email,*numbers = record
# print(numbers)
*trailing,current = [10,8,7,1,9,5,10,3]
# print(trailing,current)

name,*_,(year,*_) = data # 实现丢弃操作
# print(name,year)
 
items = [1,10,7,4,5,9]
def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head

if __name__ == "__main__":
    print(sum())

