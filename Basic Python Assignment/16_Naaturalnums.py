n = int(input("Enter n for sum of first n natural numbers: "))
if n<=0:
    print("Not natural number")
else:
    sum = (n*(n+1))/2
    print("Sum :", sum)