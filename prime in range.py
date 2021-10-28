numb = int(input("enter range"))


for num in range(2, numb):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)