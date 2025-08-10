def normalizar_telefonos(numeros, pais_defecto):
    prefijos = {"PE": "+51", "AR": "+54", "CL": "+56"}
    if pais_defecto not in prefijos:
        return {"válidos": [], "invalidos": ["NO VÁLIDOS", "Prefijo de país no soportado"]}

    validos = []
    invalidos = ["NO VÁLIDOS"]



