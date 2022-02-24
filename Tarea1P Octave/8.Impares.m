#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nNumeros impares:\n')
numero_uno = input('Ingese el numero: ');

secuencia=numero_uno:-1:1;
impares=secuencia(mod(secuencia,2)~=0);
display(impares)
pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
N=pq_exec_params(conn, "INSERT INTO impares (numero, impares) VALUES($1, $2);", {numero_uno, impares});
