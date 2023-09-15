import math

#Nestas variáveis que irá receber os coeficientes a, b e c
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

#Calcula o discriminante (delta)
delta = b**2 - 4*a*c

#Aqui Verifica os casos
if delta < 0:
    print("Não tem raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"Tem uma raiz real: {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Tem duas raízes reais: {raiz1} e {raiz2}")
