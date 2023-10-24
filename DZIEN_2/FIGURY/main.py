from trojkat import Trojkat
from prostokat import Prostokat

tr = Trojkat(5.6,6.8)
print(f'pole figury {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2')
print("_"*50)

pr1 = Prostokat(4.5,7.7)
print(f'pole figury {pr1.__class__.__name__} wynosi: {pr1.policz_pole():.2f} cm2')
print(type(pr1))
print("_"*50)

pr2 = Prostokat(5.5,5.5)
print(f'pole figury {pr2.__class__.__name__} wynosi: {pr2.policz_pole():.2f} cm2')
print(type(pr2))
print(pr2.bok)
print("_"*50)
