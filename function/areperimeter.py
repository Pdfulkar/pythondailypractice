def rectareaperim():
    a=int(input("enter the length :"))
    b=float(input("enter the breadth :"))
    if (a>=0 and b>=0):
        area=a*b
        peri=2*(a+b)
        print("The Sides of Rectangle {},{} have area :: {} and perimeter :: {}".format(a,b,area,peri))

    else:
        print("The values are invalid")
while(True):
    print(rectareaperim())
    print("Try Different Values !!!!!")