num=int(input("Enter the number:"))
x=1
if num < 0:
     print("Square root of a negative number is not a real number")
else:
    for i in range(num):
        if num==(x*x):
            break
        x=x+1
    x= (x+num/x)/2
    err=abs(num-x**2)
    if err==0:
        print("The Square root of the ",num ,"is",x)
