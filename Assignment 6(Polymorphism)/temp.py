from temperature.celsius import f_to_c as ftoc
from temperature.fahrenheit import c_to_f as ctof
from temperature.kelvin import c_to_k as ctok

print("\n--- Temperature Converter ---")
print("1) C → F")
print("2) F → C")
print("3) C → K")

option = int(input("Choose (1-3): "))

if option == 1:
    c = float(input("Celsius: "))
    print(f"Result: {ctof(c)} °F")

elif option == 2:
    f = float(input("Fahrenheit: "))
    print(f"Result: {ftoc(f)} °C")

elif option == 3:
    c = float(input("Celsius: "))
    print(f"Result: {ctok(c)} K")

else:
    print("Invalid selection!")