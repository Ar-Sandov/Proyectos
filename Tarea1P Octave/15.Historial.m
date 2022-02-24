#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf("\nOpciones de historial")
printf("\n1 - Comparacion de numeros")
printf("\n2 - Numeros de 2 en 2")
printf("\n3 - Numero y sus divisores")
printf("\n4 - Lista del mayor al menor")
printf("\n5 - Vocales de palabras")
printf("\n6 - Cantidad de cada vocal")
printf("\n7 - Suma de todas las unidades de un numero")
printf("\n8 - Numeros impares de un numero")
printf("\n9 - Area de figuras")
printf("\n10 - Tipo de triangulo")
printf("\n11 - Promedio de notas")
printf("\n12 - Factorial, si el numero es divisible entre 7")
printf("\n13 - Año bisiesto")
printf("\n14 - Clasificacion de taxis\n")

pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
 
numero_uno = input('Ingrese la opcion: ');

if (numero_uno==1)
   N=pq_exec_params(conn, 'select * from comparacion_de_numeros;')
  
  elseif (numero_uno==2)
  N=pq_exec_params(conn, 'select * from numeros_2_en_2;')
  
  elseif (numero_uno==3)
  N=pq_exec_params(conn, 'select * from divisores;')

  elseif (numero_uno==4)
  N=pq_exec_params(conn, 'select * from lista_mayor_menor;')

  elseif (numero_uno==5)
  N=pq_exec_params(conn, 'select * from contar_vocales;')

  elseif (numero_uno==6)
  N=pq_exec_params(conn, 'select * from vocales_especificas;')

  elseif (numero_uno==7)
  N=pq_exec_params(conn, 'select * from suma_hasta;')

  elseif (numero_uno==8)
  N=pq_exec_params(conn, 'select * from impares;')

  elseif (numero_uno==9)
  N=pq_exec_params(conn, 'select * from area_figuras;')

  elseif (numero_uno==10)
  N=pq_exec_params(conn, 'select * from tipo_triangulo;')

  elseif (numero_uno==11)
  N=pq_exec_params(conn, 'select * from notas_promedio;')

  elseif (numero_uno==12)
  N=pq_exec_params(conn, 'select * from factorial_7;')

  elseif (numero_uno==13)
  N=pq_exec_params(conn, 'select * from bisiesto_año;')

  elseif (numero_uno==14)
  N=pq_exec_params(conn, 'select * from taxis;')  
endif
