"""
3. Generar un nuevo entorno virtual (4 ptos)
Reglas:
- El nombre del entorno virtual tiene que seguir la siguiente estructura
(apellido_nombre) (mostrar captura de pantalla del entorno virtual vacío)
- Instalar las librerías del requirements.txt obtenido en el problema anterior en
este nuevo entorno virtual
- Mostrar las librerías instaladas en el nuevo entorno virtual (screemshot)
- Mostrar el proceso de instalación exitoso de todas las dependencias que se
verá en la terminal sobre este nuevo entorno virtual.
- Caso: Calculadora de propinas
Crea un programa que permita ingresar el total de una cuenta en un restaurante,
el porcentaje de propina que desea dejar el cliente y el número de personas que
dividirán la cuenta. El programa debe mostrar:
El monto total con propina.
El monto que debe pagar cada persona (con 2 decimales).
Un mensaje será personalizado, indicará si el monto individual supera los 100
soles, mostrando un mensaje de advertencia si es el caso.
Entrada esperada (por input):
Total de la cuenta: float
Porcentaje de propina: float
Número de personas: int
Salida ejemplo (output):
Monto total con propina: S/. 230.00
Cada persona debe pagar: S/. 115.00
¡Advertencia! El monto por persona supera los S/. 100
"""
totalCuenta = float(input("Total de la cuenta: S/"))
porcentaje = float(input("Porcentaje de propina:"))
npersonas = int(input("Numero de personas que dividiran la cuenta: "))

propina = totalCuenta * (porcentaje/100)

montoTotal = totalCuenta + propina
montoPersona = montoTotal / npersonas

print ("El monto total con propina es: S/", round(montoTotal, 2))
print ("Cada persona debe pagar: S/", round(montoPersona,2))

if montoPersona > 100:
    print(" ")
    print("¡Advertencia! El monto por persona supera los S/. 100")
