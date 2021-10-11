num1 = input("enter the number1:\n")
num2 = input("enter the number2:\n")
num3 = input("enter the number3:\n")
num4 = input("enter the number4:\n")

if(num1>num4):
    f1 = num1
else:
    f1=num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):    
    print(f1 + "is gretest")
else:
    print(f2 + "is gretest")    
