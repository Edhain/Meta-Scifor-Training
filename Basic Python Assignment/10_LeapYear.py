a = int(input("Enter a year: "))
if a%100==0:
    if a%400==0:
        print("Leap Year")
    else:
        print("Not Leap Year")
else:
    if a%4==0:
        print("Leap Year")
    else:
        print("Not Leap Year")