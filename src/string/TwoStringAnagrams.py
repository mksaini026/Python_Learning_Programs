s1 = 'triangle'
s2 = 'integral'

print(sorted(s1))
print(sorted(s2))

print(''.join(sorted(s1)))
print(''.join(sorted(s2)))

if sorted(s1) == sorted(s2):
    print('both strings are anagrams')
else:
    print('both strings are not anagrams')
