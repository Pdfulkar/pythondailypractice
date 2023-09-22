string = input()
max_no = int(input())
str1= []
for i in range(0,len(string),max_no):
    str1.append(string[int(i), (int(i) + max_no)])
print(str1)
