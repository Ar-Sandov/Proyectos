#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nLista de mayor a menor\n')
numero_uno = input('Ingese el numero mayor: ');
numero_dos = input('Ingese el numero menor: ');

secuencia=numero_uno:-1:numero_dos
pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
N=pq_exec_params(conn, "INSERT INTO lista_mayor_menor (mayor, menor, secuencia) VALUES($1, $2, $3);", {numero_uno, numero_dos, secuencia});
