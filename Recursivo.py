def factorial(n):
    r=1
    i=2
    while i<=n:
        r*=i
        i+=1
    return r
print (factorial(5))