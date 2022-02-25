#Primer Parcial
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176

import psycopg2
import numpy as npobject
import random

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "a123b",
        dbname = "Calculadora"
    )
    print("Conexion OK")
except psycopg2.Error as e:
    print("Error de conexion")

cursor = conexion.cursor()

def calculadora(operacion):
    numero_uno = ()
    numero_dos = ()
    resultado = ()
    resultado2 = ()
    resultado3 = ()
  

    #cursor = conexion.cursor()
    #cursor.execute("INSERT INTO datos(operacion, numero_uno, numero_dos, resultado) VALUES('suma',%s,%s,%s);",(numero_uno, numero_dos, resultado))
    #conexion.commit()
    #cursor.close()
    #conexion.close()

    if operacion == 1:
        try:
            numero_uno = int(input("1. Tirar dados: "))
            #numero_dos = int(input(""))
        except ValueError:
            print("Ese no es un número")
        else:
            if numero_uno==1:
                resultado=random.randint(1,6)
                print("Dado 1: "+str(resultado))
                resultado2=random.randint(1,6)
                print("Dado 2: "+str(resultado))
                resultado3=resultado+resultado2
                if resultado3==7:
                    print("perdiste")
                    resultado=0
                    resultado2=0
                elif resultado3==8:
                    print("Ganaste")
                    resultado=0
                    resultado2=0
                else:
                    print("Vuelve a jugar?")
                    resultado=0
                    resultado2=0

            #cursor.execute("INSERT INTO datos(operacion, numero_uno, numero_dos, resultado) VALUES('suma',%s,%s,%s);",(numero_uno, numero_dos, resultado))
            #conexion.commit()
            
    elif operacion == 2:
        try:
            numero_uno = int(input("Ingrese el minuendo: "))
            numero_dos = int(input("Ingrese el sustraendo: "))
        except ValueError:
            print("Ese no es un número")
        else:
            resultado = numero_uno - numero_dos
            print("El resultado de la resta es : " + str(resultado))
            cursor.execute("INSERT INTO datos(operacion, numero_uno, numero_dos, resultado) VALUES('resta',%s,%s,%s);",(numero_uno, numero_dos, resultado))
            conexion.commit()

    elif operacion == 3:
        try:
            numero_uno = int(input("Ingrese el multiplicando: "))
            numero_dos = int(input("Ingrese el multiplicador: "))
        except ValueError:
            print("Ese no es un número")
        else:
            resultado = numero_uno * numero_dos
            print("El resultado de la multiplicacion es : " + str(resultado))
            cursor.execute("INSERT INTO datos(operacion, numero_uno, numero_dos, resultado) VALUES('multiplicacion',%s,%s,%s);",(numero_uno, numero_dos, resultado))
            conexion.commit()

    elif operacion == 4:
        try:
            numero_uno = int(input("Ingrese el dividendo: "))
            numero_dos = int(input("Ingreso el divisor: "))
        except ValueError:
            print("Ese no es un número")  
        else:
            resultado = numero_uno / numero_dos
            print("El resultado de la división es : " + str(resultado))
            cursor.execute("INSERT INTO datos(operacion, numero_uno, numero_dos, resultado) VALUES('division',%s,%s,%s);",(numero_uno, numero_dos, resultado))
            conexion.commit()

    elif operacion == 5:
        try:
            numero_uno = int(input("Ingrese la base: "))
            numero_dos = int(input("Ingrese el exponente: "))
        except ValueError:
            print("Ese no es un número")
        else:
            resultado = (numero_uno**numero_dos)
            print("El resultado de la potencia es : " + str(resultado))
            cursor.execute("INSERT INTO datos(operacion, numero_uno, numero_dos, resultado) VALUES('potencia',%s,%s,%s);",(numero_uno, numero_dos, resultado))
            conexion.commit()

    elif operacion == 6:
        try:
            numero_uno = int(input("Ingrese el radicando: "))
            numero_dos = int(input("Ingrese el indice: "))
        except ValueError:
            print("Ese no es un número")
        else:
            resultado = resultado = (numero_uno**(1/numero_dos))
            print("El resultado de la raíz es : " + str(resultado))
            cursor.execute("INSERT INTO datos(operacion, numero_uno, numero_dos, resultado) VALUES('raiz',%s,%s,%s);",(numero_uno, numero_dos, resultado))
            conexion.commit()
    
    elif operacion == 7:
        SQL = 'SELECT*FROM datos;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    
    elif operacion == 8:
        SQL = "DELETE FROM datos"
        cursor.execute(SQL)
        print("Datos borrados")

if __name__ == '__main__':
    print("              Primer Parcial")
    print("   Proyectos de computación aplicados a IE")

    while True:
        try:
            print("Estas son las opciones que se pueden realizar")
            print("1 - Juego simulado del Gran 8")
            print("2 - Calificaciones")
            print("3 - Iva")
            print("4 - Numero primo o compuesto")
            print("5 - Historial")
            print("6 - Borrar historial")

            operacion = int(input("Introduce el numero de la opcion que desea realizar: "))
            calculadora(operacion)
        except ValueError:
            print("Ese no es un número")
        
        continuar = input("Desea realizar otra opcion? SI/NO ")

        if continuar == "NO":
            cursor.close()
            conexion.close()
            break