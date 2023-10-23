from oldresistor import OldResistor

print("_______________ klasa OldResistor _________________")
r0 = OldResistor(10.2E2)
print(r0)
print(r0.get_ohms())
r0.set_ohms(2.88E3)
print(r0.get_ohms())
