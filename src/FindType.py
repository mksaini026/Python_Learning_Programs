a = 10
b = 5.5
c = True
d = 'Manoj'
print(type(a))
print(type(b))
print(type(c))
print(type(d))

a = 10.5
print(type(a))

e = 'String' + d
print('e is', type(e))

f = 'String' + str(a)
print('f is', type(f))
print('f =', f)

g = str(a) + str(a)
print('g is', type(g))
print('g =', g)

h = a + 10
print('h is', type(h))
print('h =', h)