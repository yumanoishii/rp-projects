def even_fibo(n):
    x=0
    y=1
    curr=0
    sum=0
    while(curr<n):
        if(curr%2==0):
            sum+=curr
        curr=x+y
        x=y
        y=curr
            
    return sum

num=int(input("Please enter a number: "))
s = even_fibo(num)
print("The even fibonacci number sum <" + str(num) + " is " + str(s))