#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf("\nPromedio de notas\n")

numero_uno = input('Ingese la primer nota: ');
numero_dos = input('Ingese la segunda nota: ');
numero_tres = input('Ingese la tercera nota: ');
    pkg load database
    conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));

promedio=(numero_uno+numero_dos+numero_tres)/3
if (promedio>=60) 
    display('Aprobado')
    N=pq_exec_params(conn, "INSERT INTO notas_promedio (nota_1, nota_2, nota_3, promedio, resultado) VALUES($1, $2, $3,$4,'Aprobado' );", {numero_uno, numero_dos, numero_tres, promedio, numero_tres});

    else
    display('Reprobado')
    N=pq_exec_params(conn, "INSERT INTO notas_promedio (nota_1, nota_2, nota_3, promedio, resultado) VALUES($1, $2, $3,$4,'Reprobado' );", {numero_uno, numero_dos, numero_tres, promedio, numero_tres});

    endif