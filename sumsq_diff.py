def sumsq_diff(n):
    sumsq=(n*(n+1)*(2*n+1))/6 #formula for sum of squares
    sqsum=(n*(1+n)/2)**2 #formula for squares of sums
    diff=sqsum-sumsq #difference between the two
    #diff=abs((3*n**2 + 2*n) * (1 - n**2) / 12) #overall formula combining both
    return diff

num = int(input("Please enter a number: "))
d=sumsq_diff(num)
print("The sum square difference of first " + str(num) +" numbers is " + str(d))
