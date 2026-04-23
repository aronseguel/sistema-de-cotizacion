# 1. Mensaje de bienvenida inicial
nombre = input("Ingrese su nombre: ")
print(f"Hola, {nombre}! Bienvenido al sistema de cotización.")

# 2. DEFINICIÓN DE FUNCIONES (Las recetas que usaremos después)
def cotizar_proyecto():
    # Aquí adentro usamos el try/except para que no se rompa si ponen letras
    while True:
        try:
            horas = int(input("¿Cuántas horas estima que tomará el proyecto? "))
            tarifa = float(input("¿Cuál es su tarifa por hora? "))
            break # Si los números están bien, rompemos este pequeño bucle y avanzamos
        except ValueError:
            print("Error: Por favor ingresa números válidos, no letras.")
    
    costo_total = horas * tarifa

    # Lógica matemática
    if costo_total < 500:
        print(f"Costo: ${costo_total}. El proyecto es demasiado pequeño, no lo aceptamos.")
    elif costo_total >= 500 and costo_total < 1000:
        print(f"Costo: ${costo_total}. El proyecto se acepta al precio calculado.")
        guardar_en_archivo(horas, tarifa, costo_total)
    elif costo_total >= 1000:
        precio_final = costo_total * 0.90
        print(f"Costo base: ${costo_total}. Con descuento del 10%, el precio final es ${precio_final}.")
        guardar_en_archivo(horas, tarifa, precio_final)

def guardar_en_archivo(horas, tarifa, costo_final):
    # Función extra solo para mantener limpio el código. Usa "a" (Append).
    with open("cotizaciones.txt", "a") as archivo:
        archivo.write(f"Proyecto cotizado: {horas} horas a ${tarifa}/hora. Costo total: ${costo_final}\n")

def mostrar_cotizaciones():
    # En lugar de leer una lista en memoria RAM, ahora leemos el archivo del disco duro
    try:
        with open("cotizaciones.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido == "":
                print("El archivo está vacío. No hay cotizaciones.")
            else:
                print("\n--- HISTORIAL DE COTIZACIONES ---")
                print(contenido)
                print("---------------------------------")
    except FileNotFoundError:
        print("Aún no se ha creado el archivo de cotizaciones. Cotiza un proyecto primero.")

# 3. EL BUCLE PRINCIPAL (El motor del programa que mantiene todo vivo)
while True:
    print("\nOpciones:")
    print("1. Cotizar un proyecto")
    print("2. Ver cotizaciones realizadas")
    print("3. Salir")
    
    eleccion = input("Seleccione una opción: ")
    
    if eleccion == "1":
        cotizar_proyecto()
    elif eleccion == "2":
        mostrar_cotizaciones()
    elif eleccion == "3":
        print("Gracias por usar el sistema de cotización. ¡Hasta luego!")
        break # Esto apaga el motor principal y cierra la app
    else:
        # Reemplaza tu try/except. Atrapa cualquier texto raro (ej: "pepito")
        print("Opción no válida. Por favor, ingrese 1, 2 o 3.")