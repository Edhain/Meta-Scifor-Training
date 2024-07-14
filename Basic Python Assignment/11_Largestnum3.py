a,b,c=map(float, input("Enter 3 different numbers: ").split())
if a>b and a>c:
    print("largest number:", a)
elif b>a and b>c:
    print("largest number:", b)
elif c>a and c>b:
    print("largest number:", c)
else:
    print("two or more numbers same")
    