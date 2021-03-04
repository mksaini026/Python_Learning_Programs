# s1 = 'Manoj'
# s2 = 'Monik'
# i,j = 0,0
# output = ''
# while i < len(s1) or j < len(s2) :
#     output = output + s1[i] + s2[j]
#     i += 1
#     j += 1
# print(output)

s1 = 'Manoj'
s2 = 'Monikasaini'
i,j = 0,0
output = ''
while i < len(s1) or j < len(s2) :
    if i<len(s1) :
        output = output + s1[i]
        i += 1
    if j< len(s2) :
        output = output + s2[j]
        j += 1
print(output)