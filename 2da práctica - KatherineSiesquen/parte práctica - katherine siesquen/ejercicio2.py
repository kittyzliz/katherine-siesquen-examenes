"""
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""
def normalizar_nombres(lista_nombres):
    nombres_limpios = []
    nombres_vistos = set()

    for registro in lista_nombres:
        if not isinstance(registro, str):
            continue

        nombres_separados = registro.strip().split()

        for nombre_individual in nombres_separados:
            nombre_formateado = nombre_individual.title()
            if nombre_formateado not in nombres_vistos:
                nombres_limpios.append(nombre_formateado)
                nombres_vistos.add(nombre_formateado)

    return nombres_limpios

entrada_nombres = [
    "  kathe", "    liZ", "   ariana  ", "luciana",
    "ARNOLD", " JUaN", "PEDRO"
]

resultado = normalizar_nombres(entrada_nombres)

print("Original:", entrada_nombres)
print("Normalizado:", resultado)