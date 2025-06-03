# Ejercicio 1: Suma de dos números
def ejercicio1():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    suma = num1 + num2
    print(f"La suma es: {suma}")

# Ejercicio 2: Conversión de grados Celsius a Fahrenheit
def ejercicio2():
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius * 1.8 + 32
    print(f"{celsius}°C son {fahrenheit}°F")

# Ejercicio 3: Área de un triángulo
def ejercicio3():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

# Ejercicio 4: Par o impar
def ejercicio4():
    num = int(input("Ingrese un número entero: "))
    if num % 2 == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")

# Ejercicio 5: Intercambiar valores entre dos variables sin usar una tercera variable
def ejercicio5():
    a = input("Ingrese el valor de a: ")
    b = input("Ingrese el valor de b: ")
    print(f"Antes del intercambio: a = {a}, b = {b}")
    a, b = b, a  # Intercambio usando asignación múltiple
    print(f"Después del intercambio: a = {a}, b = {b}")

# Ejercicio 6: Calculadora simple
def ejercicio6():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    if num2 != 0:
        print(f"División: {num1 / num2}")
    else:
        print("No se puede dividir por cero")

# Ejercicio 7: Edad en años, meses y días
def ejercicio7():
    años = int(input("Ingrese su edad en años: "))
    meses = años * 12
    dias = años * 365  # Aproximado sin contar años bisiestos
    print(f"Tienes aproximadamente {meses} meses y {dias} días")

# Ejercicio 8: Número mayor entre tres números
def ejercicio8():
    nums = []
    for i in range(1, 4):
        n = float(input(f"Ingrese el número {i}: "))
        nums.append(n)
    mayor = max(nums)
    print(f"El número mayor es: {mayor}")

# Ejercicio 9: Verificar si un número es múltiplo de otro
def ejercicio9():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if num2 == 0:
        print("El segundo número no puede ser cero")
        return
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}")
    else:
        print(f"{num1} NO es múltiplo de {num2}")

# Ejercicio 10: Salario con bonificación
def ejercicio10():
    salario = float(input("Ingrese el salario base: "))
    bono = salario * 0.10
    total = salario + bono
    print(f"El salario total con bono es: {total}")

# Función principal para ejecutar todos los ejercicios
def main():
    print("Ejercicio 1")
    ejercicio1()
    print("\nEjercicio 2")
    ejercicio2()
    print("\nEjercicio 3")
    ejercicio3()
    print("\nEjercicio 4")
    ejercicio4()
    print("\nEjercicio 5")
    ejercicio5()
    print("\nEjercicio 6")
    ejercicio6()
    print("\nEjercicio 7")
    ejercicio7()
    print("\nEjercicio 8")
    ejercicio8()
    print("\nEjercicio 9")
    ejercicio9()
    print("\nEjercicio 10")
    ejercicio10()

if __name__ == "__main__":
    main()
