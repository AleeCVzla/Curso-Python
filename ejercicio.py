def pedir_calificaciones():
    calificaciones = []
    cantidad = int(input("¿Cuántas calificaciones vas a ingresar? "))

    for i in range(cantidad):
        nota = float(input(f"Ingrese la calificación #{i + 1}: "))
        while nota < 0 or nota > 20:
            print("X Esta calificación es inválida. Debe estar entre 0 y 20.")
            nota = float(input(f"Reingrese la calificación #{i + 1}: "))
        calificaciones.append(nota)
    
    return calificaciones

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def mostrar_resultado(promedio):
    print(f"Tu promedio final de calificacion es: {promedio:.2f}")
    if promedio >= 10:
        print(" ¡Felicidades Aprobaste!")
    else:
        print(" Debes esforzarte mas no aprobado. ¡Sigue intentando!")

def main():
    print("=== Soy tu calculadora de Promedio ===")
    calificaciones = pedir_calificaciones()
    promedio = calcular_promedio(calificaciones)
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()