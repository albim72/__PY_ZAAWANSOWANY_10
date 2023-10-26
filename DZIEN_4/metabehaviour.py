import types

def notify(fn,*args,**kwargs):
    def fncomposite(*args,**kwargs):
        print(f'{fn.__name__} została uruchomiona...')
        rt = fn(*args,**kwargs)
        return rt
    return fncomposite

# fncomposite = wrapper

class Notifies(type):
    def __new__(cls, clasname, bases, attrs):
        for name,value in attrs.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attrs[name] = notify(value)
        return super(Notifies,cls).__new__(cls, clasname, bases, attrs)

class Math(metaclass=Notifies):

    def multi(a,b,c):
        p = a*b*c
        print(p)
        return p

    @property
    def differ(self):
        return 34342

Math.multi(5,2,8)
# Math.differ(5,3)

class Info(metaclass=Notifies):
    def intro(self):
        print('to jest ważna informacja!')

i = Info()
i.intro()

mt =Math()
print(mt.differ)







