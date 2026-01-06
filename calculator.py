#Basic calculator using python

#There are two variables below to get operands

num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))

operator = input("Select the operator that you want operat '+,-,*,/'")

#Here Addition of two numbers 

if operator == '+' :
    print("Summation of first and second number is :", num1 + num2)

#Here Difference or Subtraction are calculated

elif operator == '-' :
    decision = input("If you want the difference between this numbers then select 'y' and if not then 'n' ")
    if decision == 'y' :

        #Converting nigetive(if they are!!!) numbers to positive number 

        num1 = -num1 if num1<0 else num1
        num2 = -num2 if num2<0 else num2
        if num1 > num2 :
            print("Difference between these numbers is :", num1 - num2)

        else :
            print("Difference between these numbers is :", num2 - num1)

    else :
        print("Subtraction between these numbers is :", num1 - num2)

#Here Multiplication of two numbers

elif operator == '*' :
    print("Multiplication of first and second number is :", num1 * num2)

#Here Division of the greater number by the smaller number

else :
    print("Division of ",num1," and ",num2," is :", num1 / num2)