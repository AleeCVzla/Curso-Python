def verificar(number):

        if number == 10:
            return "El numero que ud ingreso es el 10"
        elif number % 2 == 0:
            return "Su numero es PAR"
        elif number == 7:
            return "Este es un Comodin"

        else:
            return "Su numero es IMPAR" 
def main():
    number = int(input("Ingresa un numero"))
    verificar(number)
    print(verificar(number))
             
if __name__ == "__main__":
    main()          