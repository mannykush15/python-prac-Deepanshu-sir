def even(a,b):
    li = [i for i in range(a, b+1) if i % 2 == 0]
    print(li)


even(a=int(input("enter lower")),b=int(input("enter upper")))