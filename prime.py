n=int(input("Enter a number: "))
if n<=1:
        print("Prime number is greater then '1' ")
else:
        for i in range(2,n-1):
                if n%i==0:
                        print(n,"is not a prime number")
                        break;
        else:
                print(n,"is a prime number")
