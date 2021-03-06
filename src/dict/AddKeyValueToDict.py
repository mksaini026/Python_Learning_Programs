d = {}
print(len(d))
d[100] = 'manoj'
print(len(d))
print(d)

print(d.get(100))

d1 = {}
d1[200] = 'kumar'
d1[300] = 'saini'

print(d1)

print(d.update(d1))
print(d)
print(d1)
