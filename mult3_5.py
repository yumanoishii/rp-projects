
def mult3_5(n):
    sum=0
    for i in range(0, n):
        if i%3 == 0:
            sum+=i
        else:
            if i%5 == 0:
                sum+=i
            
    return sum

num = int(input("Please enter a number: "))
s = mult3_5(num)
print("The sum of the multiples of 3 and 5 of " + str(num) + " is: " + str(s))
            
    
    