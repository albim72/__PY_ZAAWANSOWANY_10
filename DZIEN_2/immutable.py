class PostiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped = 0
        pos_number = []
        for x in numbers:
            if x>=0:
                pos_number.append(x)
            else:
                skipped += 1
        instance = super().__new__(cls,pos_number)
        instance._skipped = skipped
        return instance

posnb = PostiveTuple(9,4,-9,8,13,45,0,-5,-3,12,-77,67,1,-3)
print(type(posnb))
print(posnb)
print(posnb._skipped)
