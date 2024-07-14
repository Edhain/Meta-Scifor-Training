def main():
    n1 =0
    n2 =1
    n = int(input("Enter a number :\n"))

    if n<=0:
        print("Enter a positive number")
        return
    elif n==1:
        print(0)
        return

    print(n1)
    print(n2)

    for i in range(2, n):
        n3 = n2 + n1
        print(n3)
        n1, n2 = n2, n3
        
if __name__=="__main__":
    main()