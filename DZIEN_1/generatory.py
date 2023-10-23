#przykład 1

def liczby():
    for i in range(17):
        yield i*2

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)


#przykład 2

def wznowienia(n,k):
    print("wstrzymanie działania 0")
    yield 1005
    print("wznowienie działania 1")

    print("wstrzymanie działania 1")
    yield n+k
    print("wznowienie działania 2")
    n = 8*k-2

    print("wstrzymanie działania 2")
    yield n-k
    print("wznowienie działania 3")

    print("wstrzymanie działania 3")
    yield n*k
    print("wznowienie działania 4")

    print("wstrzymanie działania 4")
    yield n**k
    print("wznowienie działania 5")

print(wznowienia(6,7))
print(tuple(wznowienia(6,7)))

print("____________________________________________")
for i in wznowienia(8,7):
    print("____________________________________________")
    print(type(i))
    print(f'zwrócono wartość: {i}')
print("____________________________________________")

#przypadek 3

def genret():
    for i in range(27):
        if i==14:
            print("przerywamy")
            return
        else:
            yield i

for t in genret():
    print(t)

#przypadek 4

def gen():
    x = 0
    while True:
        y = yield x
        if y is None:
            x = x+1
        else:
            x=y

g = gen()
print("_"*50)
print(next(g))
print(next(g))
print(next(g))

print(g.send(121))
print(next(g))
print(next(g))
print(next(g))

print(g.send(15490))
print(next(g))
