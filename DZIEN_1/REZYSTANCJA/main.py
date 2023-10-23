from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResitance

print("_______________ klasa OldResistor _________________")
r0 = OldResistor(10.2E2)
print(r0)
print(r0.get_ohms())
r0.set_ohms(2.88E3)
print(r0.get_ohms())

print("_______________ klasa Resistor _________________")
r1 = Resistor(50E3)
r1.ohms =18.3
print(f"układ elektryczny:\noporność: {r1.ohms} omów\nnapięcie prądu: {r1.voltage} V\n"
      f"natężenie prądu: {r1.current} A\n")

print("_______________ klasa VoltageResistance _________________")

r2 = VoltageResitance(1E3)
print(f'natężenie prądu (początkowe): {r2.current} A')
r2.voltage = 39
print(f'natężenie prądu: {r2.current} A')
print(f'napięcie prądu: {r2.voltage} V')
