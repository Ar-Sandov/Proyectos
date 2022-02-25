#PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\ncalificaciones:\n')
numero_uno = input('Ingese la nota 1: ');
numero_dos = input('Ingese la nota 2: ');
numero_tres = input('Ingese la nota 3: ');
numero_cuatro = input('Ingese la nota 4: ');
numero_cinco = input('Ingese la nota 5: ');

secuencia=[numero_uno numero_dos numero_tres numero_cuatro numero_cinco];
media=mean(secuencia)
mediana=median(secuencia)
rango=max(secuencia)-min(secuencia)
moda=mode(secuencia)
desviacion_estandar=std(secuencia)
varianza=var(secuencia)

pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
N=pq_exec_params(conn, "INSERT INTO calificaciones (nota1, nota2, nota3, nota4, nota5, media, mediana, moda, rango, desviacion, varianza) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11);", {numero_uno, numero_dos, numero_tres, numero_cuatro, numero_cinco, media, mediana, moda, rango, desviacion_estandar, varianza});
