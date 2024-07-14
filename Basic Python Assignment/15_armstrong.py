def main():
    total =0
    n = int(input("Enter a number:\n"))
    temp = n
    while n>0:
        r = n%10
        total = total + (r*r*r)
        n = n//10
    
    if temp==total:
        print("Number is an Armstrong number")
    else:
        print("Number is NOT an Armstrong number")
    
    
if __name__=="__main__":
    main()