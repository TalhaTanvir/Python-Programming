num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))

if(num1<33 or num2<33 or num3<33):
    print("You are fail")
elif(num1+num2+num3)/100:
    print("you are faill due to average")
else:
    print("You are pass")
