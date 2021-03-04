s = 'Manoj Kumar Saini Monika'
l = s.split()
l1 = []
i = 0
print(l[::-1])
while i < len(l):
    if i % 2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i = i + 1
print(l1)
print(" ".join(l1))