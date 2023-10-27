
n = 100
def policz(a,b,c):
    global n
    n = (a+b)*c + n
    return n

print(policz(4,5,7))
print(n)
