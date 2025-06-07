# Esta función le corresponde a: 4

def suma(a, b):
    sumas = (a + b)
    return sumas

print(suma(3, 5))


# Esta función le corresponde a: 2
def saludar(nombre):
    print(f"{nombre} hola")
    
saludar("María")


# Esta función le corresponde a: 1
def contar_hasta(n):
    for n in range(n):
        print(n)

contar_hasta(5)


# Esta función le corresponde a: 3
def mensaje():
    tiempo = int(input("Ingrese el número de veces que desea imprimir Hola mundo: "))
    for i in range(tiempo):
        print("Hola mundo")

mensaje()
