s = input('enter word: ')
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d)

for k, v in d.items():
    print(k, ' present ', v, ' times')
