#ForLoopEx2.py
lst=[100,200,300,400,500,600]
print("By using while Loop--Forward Direction")
i=0
while(i<len(lst)):
    print(lst[i])
    i=i+1
print("By using while Loop--Backward Direction")
i=len(lst)-1
while(i>=0):
    print(lst[i])
    i=i-1
print("By using for Loop--Forward Direction")
for val in lst:
    print(val)
print("By using for Loop--backward Direction")
for val in lst[::-1]:
    print(val)
print("By using for Loop--backward Direction")
for i in range(-1,-7,-1):
    print(lst[i])
print("By using for Loop--backward Direction")
for i in range(len(lst)-1,-1,-1):
    print(lst[i])