def recur(sum):
    if sum > 0:
        return sum + recur(sum -1)
    else:
        return 0

print(recur(4))