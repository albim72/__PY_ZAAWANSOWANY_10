class MojaMeta(type):
    def __new__(cls, clsname, superclasses, attrs):
        print(f"__________ {cls.__class__.__name__} ____________")
        print(f"nazwa klasy: {clsname}")
        print(f"dzidziczone klasy: {superclasses}")
        print(f"zbiór atrybutów: {attrs}")
        return type.__new__(cls, clsname, superclasses, attrs)
    def jedynka(cls):
        return 1

class S:
    pass

class F:
    pass

class Specjalna(S,metaclass=MojaMeta):
    pass

class B(Specjalna):
    pass

class C(F,B):
    pass

cf = C
print(cf.jedynka())


