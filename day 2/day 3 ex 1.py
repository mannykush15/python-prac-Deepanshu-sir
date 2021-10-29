l1=[1,2,3,4,5,6]
l2 = [0,9,8,7,10,11]
l=[]
for x in range(len(l1)):
    if x % 2 == 0:
        l.append(l1[x])
    else:
        pass

for x in range(len(l2)):
    if x % 2 == 1:
        l.append(l2[x])
    else:
        pass

print (l)