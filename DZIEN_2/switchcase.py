class Switch(object):
    value = None
    def __new__(cls, value):
        cls.value = value
        return True

    # def __init__(self, aaa):
    #     self.aaa = aaa

def case(*args):
    return any((Switch.value==arg for arg in args))

while Switch(int(input("podaj cyfrę 0-9: "))):
    if case(0):
        print("n jest równe 0")
        break
    if case(1,4,9):
        print("n jest kwadratem innej liczby")
        break
    if case(2):
        print("n jest liczbą parzystą!")
    if case(2,3,5,7):
        print("n jest liczbą pierwszą!")
        break
    if case(6,8):
        print("n jest krtonością liczby 2")
        break
    print("pisz tylko cyfry!")
    break
