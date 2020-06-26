def git_test(a,b):
    c = ((a*a)+(b*b))**(.5)
    return float(c)

a = int(input("First Number: "))
b = int(input("Second Number: "))
print("The hypontenuse: ", git_test(a,b))

