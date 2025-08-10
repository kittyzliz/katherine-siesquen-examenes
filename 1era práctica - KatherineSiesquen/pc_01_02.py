"""2.Crear un entorno virtual y aplicar lo siguiente (4 ptos):
Reglas:
- El nombre del entorno virtual tendrá el nombre con la siguiente estructura
(apellido_nombre_edad)
- Instalar las siguientes librerías: Django: 5.0.6, fastapi: 0.112.0, numpy: 2.0.0 y
aws (última versión)
- Generar el archivo de requirements.txt (mostrar las librerías instaladas)
- Crear un segundo archivo en el cual se creará una lista vacía, para luego
agregar los datos de nombre, salario, edad, compañía y bono a esta lista vacía
(todos estos datos ya fueron obtenidos en el problema anterior)
- Caso: Reporte de calificaciones:
Se tiene un alumno con calificaciones en tres cursos:
Matemáticas: 17, Ciencia: 14, Historia: 15
Cada curso tiene un peso diferente en la nota final:
Matemáticas: 40%, Ciencia: 30%, Historia: 30%
Realizar lo que se pide a continuación:
Calcula la nota final ponderada del alumno.
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
"¿Aprobado?: True" o "¿Aprobado?: Sí"

Genera una cadena resumen que diga:
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
En caso no apruebe indicar lo contrario en los mensajes.
"""
matematica = 17
ciencia = 14
historia = 15

pesoMate= 0.4
pesoCiencia = 0.3
pesoHistoria = 0.3
estado = 0

notaPonderada = (matematica*pesoMate + ciencia*pesoCiencia + historia * pesoHistoria)
print ("La nota final es:", round(notaPonderada,1))

if notaPonderada >= 13.0:
    estado = "Aprobado"
    print ("¿Aprobado?: Sí")
else:
    estado = "Reprobado"
    print ("¿Aprobado?: No")

print(f"El estudiante obtuvo una nota final de {round(notaPonderada, 1)} y su estado final es: {estado}")
