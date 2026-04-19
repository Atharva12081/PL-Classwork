#list,tuple,set & Dictionaries

count = int(input("How many fruits do you want to enter? "))

fruit_names = []
fruit_prices = []

index = 0
while index < count:
    fruit = input("Enter fruit name (apple/banana/pineapple etc.): ")
    price = int(input("Enter its price: "))
    
    fruit_names.append(fruit)
    fruit_prices.append(price)
    
    index += 1

fruits_tuple = tuple(fruit_names)

fruit_data = dict(zip(fruit_names, fruit_prices))

unique_prices = set(fruit_prices)

option = 0
while option not in [1, 2, 3, 4]:
    print("\nChoose what you want to display:")
    print("1 -> Tuple of fruit names")
    print("2 -> List of fruit prices")
    print("3 -> Dictionary of fruits with prices")
    print("4 -> Set of unique prices")
    
    option = int(input("Enter your choice: "))
    
    if option not in [1, 2, 3, 4]:
        print("Please select a valid option!")


if option == 1:
    print("Fruits stored as tuple:", fruits_tuple)

elif option == 2:
    print("Prices stored as list:", fruit_prices)

elif option == 3:
    print("Fruit-price mapping dictionary:", fruit_data)

elif option == 4:
    print("Unique prices set:", unique_prices)


