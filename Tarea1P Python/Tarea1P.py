#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176

from asyncio.windows_events import NULL
import psycopg2
import numpy as npobject

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
    numero_tres = ()
    resultado = ()
    entrada = ()


    if operacion == 1:
        print("\nComparacion de numeros")
        try:
            numero_uno = int(input("Ingrese el primer numero: "))
            numero_dos = int(input("Ingrese el segundo numero: "))
            numero_tres = int(input("Ingrese el tercer numero: "))
        except ValueError:
            print("Ese no es un número")
        else:
            if (numero_uno > numero_dos and numero_uno > numero_tres):
                resultado = numero_uno + numero_dos + numero_tres
                print("El primer numero es el mas grande")
                print("El resultado de la suma es : " + str(resultado))
                cursor.execute("INSERT INTO comparacion_de_numeros(numero1, numero2, numero3, comparacion) VALUES(%s,%s,%s,'El No.1 es mayor');",(numero_uno, numero_dos, numero_tres))
                conexion.commit()
                

            if (numero_dos > numero_uno and numero_dos > numero_tres):
                resultado = numero_uno * numero_dos * numero_tres
                print("El segundo numero es el mas grande")
                print("El resultado de la multiplicacion es : " + str(resultado))
                cursor.execute("INSERT INTO comparacion_de_numeros(numero1, numero2, numero3, comparacion) VALUES(%s,%s,%s,'El No.2 es mayor');",(numero_uno, numero_dos, numero_tres))
                conexion.commit()
            
            if (numero_tres > numero_uno and numero_tres > numero_dos):
                print("El tercer numero es el mas grande")
                print("Los numeros son: " + str(numero_uno) + ", " + str(numero_dos) + ", " + str(numero_tres))
                cursor.execute("INSERT INTO comparacion_de_numeros(numero1, numero2, numero3, comparacion) VALUES(%s,%s,%s,'El No.3 es mayor');",(numero_uno, numero_dos, numero_tres))
                conexion.commit()
            
            if (numero_tres == numero_uno):
                print("El diferente es: " + str(numero_dos))
                cursor.execute("INSERT INTO comparacion_de_numeros(numero1, numero2, numero3, comparacion) VALUES(%s,%s,%s,'El No.2 es diferente');",(numero_uno, numero_dos, numero_tres))
                conexion.commit()
            
            if (numero_dos == numero_uno):
                print("El diferente es: " + str(numero_tres))
                cursor.execute("INSERT INTO comparacion_de_numeros(numero1, numero2, numero3, comparacion) VALUES(%s,%s,%s,'El No.3 es diferente');",(numero_uno, numero_dos, numero_tres))
                conexion.commit()
            
            if (numero_dos == numero_tres):
                print("El diferente es: " + str(numero_uno))
                cursor.execute("INSERT INTO comparacion_de_numeros(numero1, numero2, numero3, comparacion) VALUES(%s,%s,%s,'El No.1 es diferente');",(numero_uno, numero_dos, numero_tres))
                conexion.commit()
            
            if (numero_dos == numero_uno == numero_tres):
                print("Todos son iguales")
                print("Los numeros son: " + str(numero_uno) +str(numero_dos) + str(numero_tres))
                cursor.execute("INSERT INTO comparacion_de_numeros(numero1, numero2, numero3, comparacion) VALUES(%s,%s,%s,'Los 3 son iguales');",(numero_uno, numero_dos, numero_tres))
                conexion.commit()
            
    elif operacion == 2:
        print("\nNumeros de 2 en 2")
        try:
            numero_uno = int(input("Ingrese el numero de inicio: "))
            numero_dos = int(input("Ingrese el numero de fin: "))
        except ValueError:
            print("Ese no es un número")
        else:
            resultado = list(range(numero_uno, numero_dos+2, 2))
            print("El resultado es : " + str(resultado))
            cursor.execute("INSERT INTO numeros_2_en_2(inicio, fin, secuencia) VALUES(%s,%s,%s);",(numero_uno, numero_dos, resultado))
            conexion.commit()

    elif operacion == 3:
        print("\nNumero y sus divisores")
        try:
            numero_uno = int(input("Ingrese el numero: "))
        except ValueError:
            print("Ese no es un número")  
        else:
            print(f"Los divisores de {numero_uno} son ", end="")
            for i in range(1, numero_uno + 1):
                if numero_uno % i == 0:
                    print(i, end=" ")
                resultado = list(range(numero_uno))
            cursor.execute("INSERT INTO divisores(numero, divisores) VALUES(%s,%s);",(numero_uno, resultado))
            conexion.commit()

    elif operacion == 4:
        print("\nLista del mayor al menor")
        try:
            numero_uno = int(input("Ingrese el primer numero: "))
            numero_dos = int(input("Ingrese el segundo numero: "))
        except ValueError:
            print("Ese no es un número")  
        else:
            if (numero_uno > numero_dos):
                resultado = list(range(numero_uno, numero_dos-1, -1))
                print("El mayor es " +str(numero_uno)+": " + str(resultado))
                cursor.execute("INSERT INTO lista_mayor_menor(mayor, menor, secuencia) VALUES(%s,%s,%s);",(numero_uno, numero_dos, resultado))
                conexion.commit()
            if (numero_dos > numero_uno):
                resultado = list(range(numero_dos, numero_uno-1, -1))
                print("El mayor es " +str(numero_dos)+": "+ str(resultado))
                cursor.execute("INSERT INTO lista_mayor_menor(mayor, menor, secuencia) VALUES(%s,%s,%s);",(numero_dos, numero_uno, resultado))
                conexion.commit()

    elif operacion == 5:
        print("\nVocales de palabras")
        try:
            entrada = input("Ingrese la palabra: ")
        except ValueError:
            print("Esa no es una palabra")
        else:
            def vocales(entrada):
                entrada = entrada.lower()
                contador = 0
                for cad in entrada:
                    if cad in "aeiou":
                        contador += 1
                return contador
        print('cantidad de vocales:',vocales(entrada))
        cursor.execute("INSERT INTO contar_vocales(palabra, vocales) VALUES(%s,%s);",(entrada, vocales(entrada)))
        conexion.commit()

    elif operacion == 6:
            print("\nCantidad de vocales")
            try:
                entrada = input("Ingrese la palabra: ")
            except ValueError:
                print("Esa no es una palabra")
            else:
                entrada = entrada.lower()
                vocales = ["a", "e", "i", "o", "u"]
                for x in vocales:
                    veces=0
                    for y in entrada: 
                        if x==y:
                            veces+=1
                    print(x, "=", veces)
                    cursor.execute("INSERT INTO vocales_especificas(palabra, vocal, veces) VALUES(%s,%s,%s);",(entrada, x, veces))
                    conexion.commit() 
                

    elif operacion == 7:
        print("\nSuma de todos los numeros hasta:")
        try:
            numero_uno = int(input("Ingrese el numero: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            resultado = list(range(0, numero_uno+1, 1))
            suma_de_num = 0
            for nota in resultado:
                suma_de_num += nota
            print("La suma de los numeros desde 0 a " +str(numero_uno)+" es: " + str(suma_de_num))
            cursor.execute("INSERT INTO suma_hasta(numero, sumatoria) VALUES(%s,%s);",(numero_uno, suma_de_num))
            conexion.commit()
    
    elif operacion == 8:
        print("\nNumeros impares")
        try:
            numero_uno = int(input("Ingrese el numero: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            resultado=list(filter((lambda x: x%2!=0),range(1,numero_uno)))
            print("los impares de "+str(numero_uno)+" son: "+str(resultado))
            cursor.execute("INSERT INTO impares(numero, impares) VALUES(%s,%s);",(numero_uno, resultado))
            conexion.commit()

    elif operacion == 9:
        print("\nEstas son las figuras que puede calcular el area")
        print("1 - Circulo")
        print("2 - Triangulo")
        print("3 - Cuadrado")
        print("4 - Rectangulo")
        try:
            numero_uno = int(input("Ingrese la figura: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            if (numero_uno==1):
                print("\nArea de circulo")
                numero_dos = int(input("Ingrese el radio: "))
                resultado = 3.141593*numero_dos*numero_dos
                redondeado = round(resultado,2)
                print("El area es "+ str(redondeado))
                cursor.execute("INSERT INTO area_figuras(figura, radio_lado1, lado2, area) VALUES('Circulo',%s,%s,%s);",(numero_dos, NULL, resultado))
                conexion.commit()
            if (numero_uno==2):
                print("\nArea de triangulo")
                numero_dos = int(input("Ingrese la base: "))
                numero_tres = int(input("Ingrese la altura: "))
                resultado = (numero_dos*numero_tres)/2
                redondeado = round(resultado,2)
                print("El area es "+ str(redondeado))
                cursor.execute("INSERT INTO area_figuras(figura, radio_lado1, lado2, area) VALUES('Triangulo',%s,%s,%s);",(numero_dos, numero_tres, resultado))
                conexion.commit()
            
            if (numero_uno==3):
                print("\nArea de cuadrado")
                numero_dos = int(input("Ingrese el lado: "))
                resultado = (numero_dos*numero_dos)
                redondeado = round(resultado,2)
                print("El area es "+ str(redondeado))
                cursor.execute("INSERT INTO area_figuras(figura, radio_lado1, lado2, area) VALUES('Cuadrado',%s,%s,%s);",(numero_dos, NULL, resultado))
                conexion.commit()

            if (numero_uno==4):
                print("\nArea de rectangulo")
                numero_dos = int(input("Ingrese el lado A: "))
                numero_tres = int(input("Ingrese el lado B: "))
                resultado = (numero_dos*numero_tres)
                redondeado = round(resultado,2)
                print("El area es "+ str(redondeado))
                cursor.execute("INSERT INTO area_figuras(figura, radio_lado1, lado2, area) VALUES('Rectangulo',%s,%s,%s);",(numero_dos, numero_tres, resultado))
                conexion.commit()
    
    elif operacion == 10:
        print("\nTipo de triangulo")
        try:
            numero_uno = int(input("Ingrese el lado a: "))
            numero_dos = int(input("Ingreso el lado b: "))
            numero_tres = int(input("Ingrese el lado c: "))
        except ValueError:
            print("Ese no es un numero")
        else:
            def tipo_de_triangulo(numero_uno, numero_dos, numero_tres):
                if numero_uno == numero_dos and numero_uno == numero_tres:
                    return 'Equilatero'
                elif numero_uno != numero_dos and numero_uno != numero_tres:
                    return 'Escaleno'
                else:
                     return 'Isosceles'
            print("El triangulo es: "+ str(tipo_de_triangulo(numero_uno, numero_dos, numero_tres)))
            cursor.execute("INSERT INTO tipo_triangulo(lado_a, lado_b, lado_c, tipo) VALUES(%s,%s,%s,%s);",(numero_uno, numero_dos, numero_tres, tipo_de_triangulo(numero_uno, numero_dos, numero_tres)))
            conexion.commit()

    elif operacion == 11:
        print("\nPromedio de notas")
        try:
            numero_uno = int(input("Ingrese la primer nota: "))
            numero_dos = int(input("Ingreso la segunda nota: "))
            numero_tres = int(input("Ingrese la tercera nota: "))
        except ValueError:
            print("Ese no es un numero")
        else:
            resultado = (numero_uno+numero_dos+numero_tres)/3
            redondeado = round(resultado,2)
            if (resultado>=60):
                print("'Aprobado' el promedio es: "+str(redondeado))
                cursor.execute("INSERT INTO notas_promedio(nota_1, nota_2, nota_3, promedio, resultado) VALUES(%s,%s,%s,%s,'Aprobado');",(numero_uno, numero_dos, numero_tres, redondeado))
                conexion.commit()
            else:
                print("'Reprobado' el promedio es: "+str(redondeado))
                cursor.execute("INSERT INTO notas_promedio(nota_1, nota_2, nota_3, promedio, resultado) VALUES(%s,%s,%s,%s,'Reprobado');",(numero_uno, numero_dos, numero_tres, redondeado))
                conexion.commit()

    elif operacion == 12:
        print("\nFactorial, si el numero es divisible entre 7")
        try:
            numero_uno = int(input("Ingrese el numero: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            if numero_uno % 7 != 0:
                print("El numero "+str(numero_uno)+" no es divisible entre 7")
            if numero_uno % 7 == 0:
                fact = 1
                for i in range(1,numero_uno+1):
                    fact = fact * i 
                print ("El factorial del numero es: ",end="")
                print (fact)            
                cursor.execute("INSERT INTO factorial_7(numero, factorial) VALUES(%s,%s);",(numero_uno, fact))
                conexion.commit()
    
    elif operacion == 13:
        print("\nAño bisiesto")
        try:
            numero_uno = int(input("Ingrese el Año: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            if numero_uno % 4 != 0: 
                resultado="No"
                print("No es bisiesto")
            elif numero_uno % 4 == 0 and numero_uno % 100 != 0: 
                resultado="Si"
                print("Es bisiesto")
            elif numero_uno % 4 == 0 and numero_uno % 100 == 0 and numero_uno % 400 != 0: 
                resultado="No"
                print("No es bisiesto")
            elif numero_uno % 4 == 0 and numero_uno % 100 == 0 and numero_uno % 400 == 0: 
                resultado="Si"
                print("Es bisiesto")            
            cursor.execute("INSERT INTO bisiesto_año(_año, bisiesto) VALUES(%s,%s);",(numero_uno, resultado))
            conexion.commit()

    elif operacion == 14:
        print("\nClasificacion de taxis")
        try:
            numero_uno = int(input("Ingrese el modelo: "))
            numero_dos = int(input("Ingrese el kilometraje: "))
        except ValueError:
            print("Ese no es un número")  
        else:
            if (numero_uno<2007 and numero_dos>20000):
                resultado="Renovar"
                print("El taxi debe renovarse")
            elif (numero_uno>=2007 and numero_uno<=2013 and numero_dos<20000):
                resultado="Mantenimiento"
                print("El taxi debe recibir mantenimiento")
            elif (numero_uno>2013 and numero_dos<10000):
                resultado="Optimo"
                print("El taxi esta en optimas condiciones")
            else:
                resultado="Mecanico"
                print("Mecanico")
            cursor.execute("INSERT INTO taxis(modelo, kilometraje, condicion) VALUES(%s,%s,%s);",(numero_uno, numero_dos, resultado))
            conexion.commit()
    
    elif operacion == 15:
        print("\nOpciones de historial")
        print("1 - Comparacion de numeros")
        print("2 - Numeros de 2 en 2")
        print("3 - Numero y sus divisores")
        print("4 - Lista del mayor al menor")
        print("5 - Vocales de palabras")
        print("6 - Cantidad de cada vocal")
        print("7 - Suma de todas las unidades de un numero")
        print("8 - Numeros impares de un numero")
        print("9 - Area de figuras")
        print("10 - Tipo de triangulo")
        print("11 - Promedio de notas")
        print("12 - Factorial, si el numero es divisible entre 7")
        print("13 - Año bisiesto")
        print("14 - Clasificacion de taxis")
        try:
            numero_uno = int(input("Ingrese la opcion: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            if (numero_uno==1):
                SQL = 'SELECT*FROM comparacion_de_numeros;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==2):
                SQL = 'SELECT*FROM numeros_2_en_2;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==3):
                SQL = 'SELECT*FROM divisores;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==4):
                SQL = 'SELECT*FROM lista_mayor_menor;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==5):
                SQL = 'SELECT*FROM contar_vocales;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==6):
                SQL = 'SELECT*FROM vocales_especificas;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==7):
                SQL = 'SELECT*FROM suma_hasta;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==8):
                SQL = 'SELECT*FROM impares;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==9):
                SQL = 'SELECT*FROM area_figuras;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==10):
                SQL = 'SELECT*FROM tipo_triangulo;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==11):
                SQL = 'SELECT*FROM notas_promedio;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==12):
                SQL = 'SELECT*FROM factorial_7;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==13):
                SQL = 'SELECT*FROM bisiesto_año;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            if (numero_uno==14):
                SQL = 'SELECT*FROM taxis;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)

    elif operacion == 16:
        print("\nOpciones a borrar")
        print("1 - Comparacion de numeros")
        print("2 - Numeros de 2 en 2")
        print("3 - Numero y sus divisores")
        print("4 - Lista del mayor al menor")
        print("5 - Vocales de palabras")
        print("6 - Cantidad de cada vocal")
        print("7 - Suma de todas las unidades de un numero")
        print("8 - Numeros impares de un numero")
        print("9 - Area de figuras")
        print("10 - Tipo de triangulo")
        print("11 - Promedio de notas")
        print("12 - Factorial, si el numero es divisible entre 7")
        print("13 - Año bisiesto")
        print("14 - Clasificacion de taxis")
        try:
            numero_uno = int(input("Ingrese la opcion: "))
            
        except ValueError:
            print("Ese no es un número")
        else:
            if (numero_uno==1):
                SQL = 'DELETE FROM comparacion_de_numeros;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==2):
                SQL = 'DELETE FROM numeros_2_en_2;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==3):
                SQL = 'DELETE FROM divisores;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==4):
                SQL = 'DELETE FROM lista_mayor_menor;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==5):
                SQL = 'DELETE FROM contar_vocales;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==6):
                SQL = 'DELETE FROM vocales_especificas;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==7):
                SQL = 'DELETE FROM suma_hasta;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==8):
                SQL = 'DELETE FROM impares;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==9):
                SQL = 'DELETE FROM area_figuras;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==10):
                SQL = 'DELETE FROM tipo_triangulo;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==11):
                SQL = 'DELETE FROM notas_promedio;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==12):
                SQL = 'DELETE FROM factorial_7;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==13):
                SQL = 'DELETE FROM bisiesto_año;'
                cursor.execute(SQL)
                print("Datos borrados")
            if (numero_uno==14):
                SQL = 'DELETE FROM taxis;'
                cursor.execute(SQL)
                print("Datos borrados")

if __name__ == '__main__':
    print("     TAREA PREPARATORIA PRIMER PARCIAL")
    print("   Proyectos de computación aplicados a IE")

    while True:
        try:
            print("\nEstas son las opciones que se pueden realizar")
            print("1 - Comparacion de numeros")
            print("2 - Numeros de 2 en 2")
            print("3 - Numero y sus divisores")
            print("4 - Lista del mayor al menor")
            print("5 - Vocales de palabras")
            print("6 - Cantidad de cada vocal")
            print("7 - Suma de todas las unidades de un numero")
            print("8 - Numeros impares de un numero")
            print("9 - Area de figuras")
            print("10 - Tipo de triangulo")
            print("11 - Promedio de notas")
            print("12 - Factorial, si el numero es divisible entre 7")
            print("13 - Año bisiesto")
            print("14 - Clasificacion de taxis")
            print("15 - Historial")
            print("16 - Borrar historial")

            operacion = int(input("Introduce el numero de la opcion que desea realizar: "))
            calculadora(operacion)
        except ValueError:
            print("Ese no es un número")
        
        continuar = input("\nDesea realizar otra opcion? si/no ")

        if continuar == "no":
            cursor.close()
            conexion.close()
            break