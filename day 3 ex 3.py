lis = [11, 45, 8, 11, 23, 45, 23, 45, 89]
x = {}
for i in lis:
    if i not in x.keys():
        x[i]=lis.count(i)
print(x)
