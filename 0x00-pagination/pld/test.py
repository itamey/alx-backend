class A:
  pass

a = A()
this = int()

num = 9

print(isinstance(this, int))
print(isinstance(a, A))

print(type(a))
print(type(this))
print(type(num))
print(type(a) == type(num))
