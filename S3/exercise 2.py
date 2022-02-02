
def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(2, n ):
            num = n1 + n2
            n1 = n2 #because my new n1 is n2
            n2 = num
        return num

print("5th Fibonacci´s term:", fib(5)) #when pass an argument as 5 then it will chane n for 5
print("11th Fibonacci´s term:", fib(11))
print("55th Fibonacci´s term:", fib(55)) #n is a position of the fibonacci sequence and n is any position so,
#what we do is to print n = 5 where 5 is not a value but the position of the value we want.