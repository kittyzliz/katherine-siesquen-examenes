"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda.
"""

nombre = "Katherine" #string
salario = 500.2 #float
edad = "20" #string
compañia = "Samsung" #string
bono = 0 #float

if int(edad) > 30:
    bono = 0.10
    print(nombre,"Usted tiene un bono de 10% en el mes de diciembre")
else:
    bono = 0.05
    print(nombre,"Usted tiene un bono del 5% en el mes diciembre")

bonoFinal = pow(salario, 2) + (salario * bono)
print("Su sueldo final en nuestra compañía",compañia, "es:", round(bonoFinal, 2))
