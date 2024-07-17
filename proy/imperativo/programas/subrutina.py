def calcular_area(base, altura):
  area = (base * altura) / 2
  return area

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = calcular_area(base, altura)
print("El área del triángulo es:", area)