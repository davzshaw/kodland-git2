def sumar_numeros():
     try:
          numero_1 = int(input("Introduce el primer número: "))
          numero_2 = int(input("Introduce el segundo número: "))
          return numero_1 + numero_2
      except ValueError:
          print("Error: Por favor, introduce solo números.")

resultado = sumar_numeros()
if resultado is not None:
     print("Resultado de la suma:", resultado)
