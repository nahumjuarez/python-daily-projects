# Diccionario y definir funciones

Milla_en_km = 1.609344

def milla_a_km(millas):
    return millas * Milla_en_km

def km_a_milla(km):
    return km / Milla_en_km

scale = 9/5 
offset = 32

def cel_to_far(celsius):
    return celsius * scale + offset

def far_to_cel(fahrenheit):
    return (fahrenheit - offset) / scale 

print("Choose the conversion you want to make:")
print("1: Kilometers to Miles")
print("2: Miles to Kilometers")
print("3: Celsius to Fahrenheit")
print("4: Fahrenheit to Celsius")

option = input("Select one option: ")
value = float(input("Enter the value to convert: "))

if option == "1":
    print(f"{value} Km = {km_a_milla(value):.2f} Miles")
elif option == "2":
    print(f"{value} Miles = {milla_a_km(value):.2f} Km")
elif option == "3":
    print(f"{value} Celsius = {cel_to_far(value):.2f} Fahrenheit")    
elif option == "4":
    print(f"{value} Fahrenheit = {far_to_cel(value):.2f} Celsius")    
else: 
    print("Invalid option")