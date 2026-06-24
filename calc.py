class Calculator:

    def sum (self ,a,b):
        return a+b
    def diff (self ,a,b):
        return a - b
    def product (self, a,b):
        return a*b
    def divide (self,a,b):
        if b!=0:
            return a/b
        else:
            return"not divisible"
print ("Enter two numbers")
a = int (input ( "enter first number"))
b = int (input ( "enter second number"))
calc = Calculator()
user_input = input(
"Enter the operation you want to perform -\n"
"ADDITION (+)\n"
"DIFFERENCE (-)\n"
"PRODUCT (*)\n"
"DIVIDE (/)\n")

if user_input == '+' :

    print ("the sum of {} and {} is {}" . format( a, b , calc.sum(a,b)))
elif user_input == '-':
    print ("the difference of {} and {} is {}" .format( a, b , calc.diff(a,b)))
elif user_input == '*':
    print ("the product of {} and {} is {}".format( a, b , calc.product(a,b)))
elif user_input == '/':
    print ("the division of {} and {} is {}" .format( a, b , calc.divide(a,b)))
else:
    print("invalid input")