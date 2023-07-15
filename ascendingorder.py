# l=[22,4,111,6,9,33]
# print(l.sort())
# print(l)

# l=[22,4,111,6,9,33]
# print(min(l))

# l=[22,4,111,6,9,33]
# l[0],l[1]=l[1],l[0]
# print(l)

# l=[22,4,111,6,9,33]
# for i in range(len(l)):
#     m=min(l[i:])
#     index=l.index(m)
#     l[i],l[index]=l[index],l[i]
# print(l)

l=[22,4,111,6,9,33]
for i in range(len(l)):
    min=l[i]
    for j in range(i+1,len(l)):
        if min>l[j]:
            min=l[j]
    index=l.index(min)
    l[i],l[index]=l[index],l[i]

print(l)
        