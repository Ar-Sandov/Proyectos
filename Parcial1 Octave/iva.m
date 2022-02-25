#PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nIVA:\n')
numero_uno = input('Ingese el precio en Q: ');

iva=numero_uno*0.12
sin_iva=numero_uno-iva
pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
N=pq_exec_params(conn, "INSERT INTO iva (precio, iva, precio_sin_iva) VALUES($1, $2, $3);", {numero_uno, iva, sin_iva});
