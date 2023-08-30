#program for demonstrating break statement
#BreakStmtEx1.py
s="PYTHON"
print("By Using for Loop")
for ch in s:
    print(ch)
else:
    print("i am from for--else loop")
print("==============================")
#My Requirment is to disp Only PYTH without using Slicing and Indexing
for ch in s:
    if(ch=="O"):
        break
    else:
        print("\t{}".format(ch))
else:
    print("i am from for--else loop")
print("Other Statements in Program")