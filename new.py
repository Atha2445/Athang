# Program to enter two numbers and
# print the arithmetic operations like +,-,*, /, // and%.

#Function for addition 
def add(x,y):
    return x + y

#Function for substraction
def sub(x,y):
    return x - y

#Function for multiplication
def multiply(x,y):
    return x * y

#Function for quotient
def divide(x,y):
    return x/y

#Function for remainder
def divide(x,y):
    return x//y

#Function for percentage
def percentage(x,y):
    return((x/y)*100)    

print('Select operation.')
print('1.add')
print('2.sub')
print('3.multiply')
print('4.quotient') 
print("5.remainder")        
print('6.percentage')   

#For choice from user
choice = input('Enter choice(1/2/3/4/5/6):')
 
if choice in ('1','2','3','4','5','6'):
    num1 = float(input('Enter first number:'))
    num2 = float(input('Enter second:'))

    if choice == '1':
        print(num1, '+', num2, '=', add(num1,num2))

    elif choice == '2':
        print(num1, '-', num2, '=', sub(num1,num2))

    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1,num2)) 

    elif choice == '4':
        print(num1, '/', num2, '=', divide(num1,num2))       

    elif choice == '5':
        print(num1, '//', num2, '=', divide(num1,num2))    

    else :
        print(num1, '%', num2, '=', percentage(num1,num2))   