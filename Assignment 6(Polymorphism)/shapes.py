import shapes as sh

print("\n--- Area Calculator ---")
print("1) Circle")
print("2) Rectangle")
print("3) Triangle")

opt = int(input("Select option (1-3): "))

if opt == 1:
    radius = float(input("Radius: "))
    result = sh.circle(radius)

elif opt == 2:
    length = float(input("Length: "))
    width = float(input("Width: "))
    result = sh.rectangle(length, width)

elif opt == 3:
    base = float(input("Base: "))
    height = float(input("Height: "))
    result = sh.triangle(base, height)

else:
    result = None
    print("Wrong selection!")

if result:
    print("Calculated Area =", result)