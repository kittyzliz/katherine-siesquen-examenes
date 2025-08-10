"""
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiantes.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio
"""
def procesar_notas(estudiantes):
    resultados = {}

    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        estado = "Aprobado" if promedio >= 11 else "Desaprobado"

        resultados[nombre] = {
            "promedio": promedio,
            "estado": estado
        }

    mejorEstudiante = max(resultados, key=lambda x: resultados[x]["promedio"])
    print(f"El estudiante con mayor promedio es {mejorEstudiante} "
          f"con {resultados[mejorEstudiante]['promedio']:.2f}\n")

    for nombre, datos in resultados.items():
        print("-" * 20)
        print(nombre)
        print(f"Promedio: {datos['promedio']:.2f}")
        print(f"Estado: {datos['estado']}")

    return resultados

estudiantes = {
    "Kath": [18, 15, 14],
    "Lizbeth": [9, 14, 8],
    "Vania": [17, 12, 19]
}

procesar_notas(estudiantes)

