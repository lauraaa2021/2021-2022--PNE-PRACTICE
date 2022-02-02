N = 11 #constant: variable whose value is never going to change. We create them at the beginning of the code
#They are denoted by capital letters

n1 = 0
n2  = 1

print(n1, end= " ")
print(n2, end= " ")
for i in range(2, N ):
    num = n1 + n2
    print(num, end=" ")
    n1 = n2 #because my new n1 is n2
    n2 = num
print()
