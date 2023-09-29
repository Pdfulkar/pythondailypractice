from array import *
arr = array ('i',[])
n = int(input("How many number do you want put in"))

for i in range (n):
    arr.append(int(input("Put in the Number = ")))
print(arr)

Num = int(input("Which numbers positino do you want to find Put that Num = "))
K = 0
for i in range(len(arr)):
    if Num == arr[i]:
        print (K)
        break
    K+=1
print(arr.index(Num))


