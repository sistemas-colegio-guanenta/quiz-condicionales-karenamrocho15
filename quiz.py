# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a =float(input( "ingresa la longitud del lado a : "))
b =float(input( "ingresa la longuitd del lado b : "))
c =float(input( "ingresa la longuitud del lado c :"))
# processing
#verificacion si las longuitudes pueden formar un triangulo
if a + b > c and a + c > b and b + c > a :
    print("estas longuitudes puedem formar un traingulo.")
else:
    print("estas longuitudes no pueden formar un triangulo.")
    


# output
