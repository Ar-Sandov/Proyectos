#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nNumeros de 2 en 2\n')
numero_uno = input('Ingese el numero de inicio: ');
numero_dos = input('Ingese el numero de fin: ');
secuencia=[numero_uno:2:numero_dos]
pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
N=pq_exec_params(conn, "INSERT INTO numeros_2_en_2 (inicio, fin, secuencia) VALUES($1, $2, $3);", {numero_uno, numero_dos, secuencia});
