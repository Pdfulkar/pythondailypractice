if __name__ == '__main__':
    N = int(input())
i=1
Ope = []
oper = []
lst = []
while(i<=N):
    INP= str(input())
    Ope.append(INP)
    i+=1
for i in range(0,len(Ope)):
    match Ope[i].split()[0]:
        case "insert":
            lst.insert(int(Ope[i].split()[1]),int(Ope[i].split()[2]))
        case "print":
            print(lst)
        case "remove":
            lst.remove(int(Ope[i].split()[1]))
        case "append":
            lst.append(int(Ope[i].split()[1]))
        case "sort":
            lst.sort()
        case "pop":
            lst.pop()
        case "reverse":
            lst.reverse()
