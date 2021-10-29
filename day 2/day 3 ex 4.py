firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
# Expected Output:
FirstSet = {57, 83, 299}
SecondSet = {67, 73, 43, 48, 83, 57, 29}

print("first set is subset of second = ", firstSet.issubset(secondSet))
print("second set is superset of first = ", secondSet.issuperset(firstSet))
print("First set is subset of Second = ", FirstSet.issubset(SecondSet))
print("Second set is superset of First = ", SecondSet.issuperset(FirstSet))

if firstSet.issubset(secondSet):
    firstSet = {}
print(firstSet, secondSet, sep='\n')