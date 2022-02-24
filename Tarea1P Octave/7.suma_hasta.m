#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nSuma de todos los numeros hasta:\n')
numero_uno = input('Ingese el numero: ');

secuencia=numero_uno:-1:numero_dos
suma=sum(sum(secuencia))
pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
N=pq_exec_params(conn, "INSERT INTO suma_hasta (numero, sumatoria) VALUES($1, $2);", {numero_uno, suma});
