#program for demonstrating break statement
#BreakStmtEx2.py
s="PYTHON"
print("By Using while Loop")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("i am from while--else loop")
print("==============================")
#My Requirment is to disp Only PYTH without using Slicing and Indexing
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print("{}".format(s[i]),end="")
    i=i+1
else:
    print("i am from while--else loop")
print()
print("Other Statements in Program")