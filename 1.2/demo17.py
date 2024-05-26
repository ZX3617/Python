x=20
y=10
x=x+y
print(x)
x+=y
x-=y
print(x)

x*=y
print(x)
x/=y
print(x)
print(type(x))
x%=2
print(x)

z=3
y//=z
print(y)

y**=2
print(y)

a=b=c=100
print(a,b,c)

a,b=10,20
print(a,b)

print('---如何交换两个变量的值呢？---')
a,b=b,a
print(a,b)