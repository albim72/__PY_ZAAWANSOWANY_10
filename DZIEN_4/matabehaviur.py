import types

def notify(fn,*args,**kwargs):
    def fncomposite(*args,**kwargs):
        print(f'{fn.__name__} została uruchomiona...')
        rt = fn(*args,**kwargs)
        return rt
    return fncomposite

# fncomposite = wrapper
