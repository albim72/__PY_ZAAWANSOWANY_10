def liczby():
    for i in range(17):
        yield i*2

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)
