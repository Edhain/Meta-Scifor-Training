a = int(input("Enter a number: "))
b=0
while a!=0:
    b=b+(a%10)
    a=a//10
    
print('Sum of digits: ', b)