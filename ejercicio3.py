class Numero:    
    def __init__(self, numero):
        self.numero = numero
        
    def evaluarNumero(self):
        if self.numero %2 != 0:
            print ("El numero ingresado es impar")
        else:
            print("El numero ingresado es par")
            
        if self.numero == 7:
            print("El numero ingresado es el 7")
        elif self.numero == 10:
            print("El numero ingresado es el 10")
            
    def sumar (self, numeroasumar):
        return self.numero + numeroasumar

if __name__ == "__main__":

    numeroaevaluar = Numero(int(input("ingrese un numero")))
    numeroaevaluar.evaluarNumero()
    sumarealizada = numeroaevaluar.sumar(5)
    print("La suma realizada es",sumarealizada) 