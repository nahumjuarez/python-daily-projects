def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicacion(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2 != 0:
        return num1 / num2
    else: 
        return "Math error"

# Menu

print("Elige la operación que quieras realizar ")
print("1: Suma")
print("2: Resta")
print("3: Multiplicación")
print("4: División")

opcion = input("¿Qué operación quieres realizar ?")

num1= float(input("Ingresa tu primer número "))
num2= float(input("Ingresa tu segundo número "))

if opcion == '1':
    print(f"{num1}+{num2}={suma(num1,num2)}")
elif opcion == '2':
    print(f"{num1}-{num2}={resta(num1,num2)}")
elif opcion == '3':
    print(f"{num1}*{num2}={multiplicacion(num1,num2)}")
elif opcion == '4':
    print(f"{num1}/{num2}={division(num1,num2)}")
else:
    print("¿Por qué el mexicano no lee?")
    
    