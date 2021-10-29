# n = int(input("enter list range"))
lis = [1,2,3,4,5,6,7,8,9]
lis1 = []
lis2 = []
lis3 = []
if len(lis) % 3 == 0:

    p = int(len(lis)/3)
    # for x in range(0, n):
    #     lis.append(int(input(f"{x} value ")))
    for x in range(0, p):
        lis1.append(lis.pop())
    for x in range(0, p):
        lis2.append(lis.pop())
    for x in range(0, p):
        lis3.append(lis.pop())
    print(lis1, lis2, lis3 , sep='\n')
else:
    print("enter length divisible by 3")



# l=[1,2,3,4,5,6]
#
# p=l.pop()
# print(p)