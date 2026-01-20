#take two number as a input and print there diffrence , sum , product , division

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

opr = input("Enter the Operator(+,-,*,/)")

if(opr == "+"):
    print(f"Sum is {num1+num2}")
elif(opr == "-"):
    if(num1>num2):
        print(f"Diffrence is {num1-num2}")
    else:
        print(f"Diffrence is {num2-num1}")
elif(opr == "*"):
    print(f"Product is {num1*num2}")
elif(opr == "/"):
    print(f"Division is {num1/num2}")
else:
    print("choose right opr")