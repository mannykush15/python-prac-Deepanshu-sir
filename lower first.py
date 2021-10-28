s=input("enter string with lower and upper characters ")
small=""
caps=""
for c in s:
    if c.islower():
        small=small+c
    else:
        caps=caps+c

print(small+caps)