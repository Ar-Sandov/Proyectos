#Primer Parcial
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176

import psycopg2
import numpy as npobject
import random
import statistics


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
    resultado = 0
    resultado2 = 0
    resultado3 = ()
    numero_tres = ()
    numero_cuatro = ()
    numero_cinco = ()
  

    #cursor = conexion.cursor()
    #cursor.execute("INSERT INTO datos(operacion, numero_uno, numero_dos, resultado) VALUES('suma',%s,%s,%s);",(numero_uno, numero_dos, resultado))
    #conexion.commit()
    #cursor.close()
    #conexion.close()

    if operacion == 1:
        try:
            numero_uno = int(input("1. Tirar dados: "))
        except ValueError:
            print("Ese no es un número")
        else:
            if numero_uno==1:
                resultado=random.randint(1,6)
                print("Dado 1: "+str(resultado))
                resultado2=random.randint(1,6)
                print("Dado 2: "+str(resultado2))
                resultado3=resultado+resultado2
                if resultado3==7:
                    print("perdiste")
                    cursor.execute("INSERT INTO dados(dado1, dado2, suma, resultado) VALUES(%s,%s,%s,'Perdiste');",(resultado, resultado2, resultado3))
                    conexion.commit()
                elif resultado3==8:
                    print("Ganaste")
                    cursor.execute("INSERT INTO dados(dado1, dado2, suma, resultado) VALUES(%s,%s,%s,'Ganaste');",(resultado, resultado2, resultado3))
                    conexion.commit()
                else:
                    print("Vuelve a jugar")
                    cursor.execute("INSERT INTO dados(dado1, dado2, suma, resultado) VALUES(%s,%s,%s,'Vuleve a jugar');",(resultado, resultado2, resultado3))
                    conexion.commit()


            
            
    elif operacion == 2:
        try:
            numero_uno = int(input("Ingrese la primer nota: "))
            numero_dos = int(input("Ingrese la segunda nota: "))
            numero_tres = int(input("Ingrese la tercer nota: "))
            numero_cuatro = int(input("Ingrese la cuarta nota: "))
            numero_cinco = int(input("Ingrese la quinta nota: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            resultado = (numero_uno + numero_dos + numero_tres + numero_cuatro + numero_cinco)/5
            print("La media es : " + str(resultado))
            lista = [numero_uno,numero_dos,numero_tres,numero_cuatro,numero_cinco]
            resultado2=statistics.median(lista)
            print("La mediana es: "+ str(resultado2))
            resultado3=statistics.mode(lista)
            print("La moda es: "+ str(resultado3))
            resultado4=(max(lista)-min(lista))
            print("El rango es: "+ str(resultado4))
            resultado5=round(statistics.pstdev(lista),2)
            print("El desviacion estadar es: "+ str(resultado5))
            resultado6=statistics.variance(lista)
            print("El varianza es: "+ str(resultado6))
            cursor.execute("INSERT INTO calificaciones(nota1, nota2, nota3, nota4, nota5, media, mediana, moda, rango, desviacion, varianza) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(numero_uno, numero_dos, numero_tres, numero_cuatro, numero_cinco, resultado, resultado2, resultado3, resultado4, resultado5, resultado6))
            conexion.commit()

    elif operacion == 3:
        try:
            numero_uno = int(input("Ingrese el precio en Q: "))
        except ValueError:
            print("Ese no es un número")
        else:
            resultado = numero_uno * 0.12
            print("El IVA es : " + str(resultado))
            resultado2=numero_uno-resultado
            print("El precio sin IVA es : " + str(resultado2))
            cursor.execute("INSERT INTO iva(precio, iva, precio_sin_iva) VALUES(%s,%s,%s);",(numero_uno, resultado, resultado2))
            conexion.commit()

    elif operacion == 4:
        try:
            numero_uno = int(input("Ingrese el numero: "))
        except ValueError:
            print("Ese no es un número")  
        else:
            valor= range(2,numero_uno)
            contador = 0
            for n in valor:
                if numero_uno % n == 0:
                    contador +=1
            if contador > 0 :
                resultado="Compuesto"
                print("El número es compuesto" )
                cursor.execute("INSERT INTO primo(numero, resultado) VALUES(%s,%s);",(numero_uno,resultado))
                conexion.commit()
            else:
                resultado="Primo"
                print("El numero es primo")
                cursor.execute("INSERT INTO primo(numero, resultado) VALUES(%s,%s);",(numero_uno,resultado))
                conexion.commit()
    
    elif operacion == 5:
        print("\nOpciones de historial")
        print("1 - Juego simulado del Gran 8")
        print("2 - Calificaciones")
        print("3 - Iva")
        print("4 - Numero primo o compuesto")
        try:
            numero_uno = int(input("Ingrese la opcion: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            if (numero_uno==1):
                SQL = 'SELECT*FROM dados;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==2):
                SQL = 'SELECT*FROM calificaciones;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==3):
                SQL = 'SELECT*FROM iva;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==4):
                SQL = 'SELECT*FROM primo;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
        
    
    elif operacion == 6:
        print("\nOpciones a borrar")
        print("1 - Juego simulado del Gran 8")
        print("2 - Calificaciones")
        print("3 - Iva")
        print("4 - Numero primo o compuesto")
        try:
            numero_uno = int(input("Ingrese la opcion: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            if (numero_uno==1):
                SQL = 'DELETE FROM dados;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==2):
                SQL = 'DELETE FROM calificaciones;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==3):
                SQL = 'DELETE FROM iva;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==4):
                SQL = 'DELETE FROM primo;'
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