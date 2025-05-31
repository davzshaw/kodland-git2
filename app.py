try:
     numero_1 = int(input("Introduce el primer número: "))
     numero_2 = int(input("Introduce el segundo número: "))
     print("Resultado de la suma:", numero_1 + numero_2)
 except ValueError:
     print("Error: Por favor, introduce solo números.")
