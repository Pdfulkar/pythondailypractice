No1 = int(input())
setA = set(map(int, input().split()))
No2 = int(input())
i = 0
while i < No2:
    list_ = list(map(str, input().split()))
    setB = set(map(int, input().split()))
    operation = list_[0]
    match operation:
        case "intersection_update":
            setA.intersection_update(setB)
        case "update":
            setA.update(setB)
        case "difference_update":
            setA.difference_update(setB)
        case "symmetric_difference_update":
            setA.symmetric_difference_update(setB)
    i+=1
print(sum(setA))