num1 = int(input("enter the marks subject1:"))
num2 = int(input("enter the marks subject2:"))
num3 = int(input("enter the marks subject3:"))


if(num1<33 or num2<33 or num3<33):
    print("YOU ARE FAIL")

if(num1 + num2 + num3)/3 <40 :
    print("you are fail")
else:
    print("you are pass")    
    