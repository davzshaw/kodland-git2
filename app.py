try:
     a = int(input("Introduce el primer número: "))
     b = int(input("Introduce el segundo número: "))
     print("Resultado de la suma:", a + b)
 except ValueError:
     print("Error: Por favor, introduce solo números.")
