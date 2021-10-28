s = input("enter string")

if (len(s) % 2 == 1) and len(s)>7 :
    n = ((len(s)-1)//2)-1
    b=n+3
    print(s[n:b])
else:
    print("enter odd length value greater than 7 characters")

