n,m = map(int, input().split())
print(n,m)
for i in range(1,n,2):
    print ("-"*((m-(i*3))//2)+ ".|."*i +"-"*((m-(i*3))//2))
print("-"*((m-7)//2)+"WELCOME"+"-"*((m-7)//2))
for i in range(n-2,0,-2):
    print ("-"*((m-(i*3))//2)+ ".|."*i +"-"*((m-(i*3))//2))