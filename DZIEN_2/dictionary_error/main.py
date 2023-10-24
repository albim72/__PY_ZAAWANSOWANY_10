#budowa słownika poprzez zadanie listy lub krotki z kluczami i wartościami
#wartości słownika mogą być reprezentowany tylko poprzez typy: int lub float

from klasybledu import InFloatValueError, KeyValueConstructError

class CustomIntFloatDict(dict):
    empty_dict = {}

    def get_dict(self):
        return self.empty_dict

    def __init__(self,key=None,value=None):
        if key is None or value is None:
            self.get_dict()
        elif not isinstance(key,(tuple,list,)) or not isinstance(value,(tuple,list,)):
            raise KeyValueConstructError(key,value)
        else:
            zipped = zip(key,value)
            for k,val in zipped:
                if not isinstance(val,(int,float,)):
                    raise InFloatValueError(val)
                dict.__setitem__(self,k,val)

    # def __setitem__(self, key, value):
    #     if not isinstance(value, (int, float,)):
    #         raise InFloatValueError(value)
    #     return dict.__setitem__(self,key,value)

test_1 = CustomIntFloatDict()
print(test_1)

test_2 = CustomIntFloatDict(('a','b'))
print(test_2)

# test_3 = CustomIntFloatDict({'a','b'},[4,6])

test_4 = CustomIntFloatDict(('x','y','z'),(23,"twenty",77))

test_5 = CustomIntFloatDict(('x','y','z'),(23,20,77))
print(test_4)
