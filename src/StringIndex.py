s = 'Manoj'
print(s[0])
print(s[3])
print(s[-1])
print(s[-5])
print(s[-2])

name = 'Manoj Kumar Saini'
print(name[0:5])  # returns sting 0 to 5-1 index
print(name[:11])  # 0 to 11-1
print(name[6:])  # 6 to end of the string
print(name[:])
print(name)
print(name[6:100000])
print('Empty string :', name[6:1])

sn = 'saini'
print(len(sn))
print(sn[:len(sn) - 1])
print(sn[0].upper() + sn[1:])
print(sn[:len(sn) - 1] + sn[-1].upper())
print(sn[0].upper() + sn[1:len(sn) - 1] + sn[-1].upper())
print(sn * 3)
print(3 * s)
