#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf("\nEstas son las figuras que puede calcular el area\n")
printf("\n1 - Circulo")
printf("\n2 - Triangulo")
printf("\n3 - Cuadrado")
printf("\n4 - Rectangulo\n")
numero_uno = input('Ingese la figura: ');
  pkg load database
  conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));


if (numero_uno==1)
  printf('\nArea de circulo\n')
  numero_dos = input('Ingese el radio: ');
  display('Circulo ')
  Area=3.141593*numero_dos*numero_dos
  N=pq_exec_params(conn, "INSERT INTO area_figuras (figura, radio_lado1, lado2, area) VALUES('Circulo', $2, 0,$4 );", {numero_dos, numero_dos, numero_tres, Area});

  elseif (numero_uno==2)
  printf('\nArea de triangulo\n')
  numero_dos = input('Ingese la base: ');
  numero_tres = input('Ingese la altura: ');
  display('Triangulo ')
  Area=(numero_dos*numero_tres)/2
  N=pq_exec_params(conn, "INSERT INTO area_figuras (figura, radio_lado1, lado2, area) VALUES('Triangulo', $2, $3,$4 );", {numero_dos, numero_dos, numero_tres, Area});

  elseif (numero_uno==3)
  printf('\nArea de cuadrado\n')
  numero_dos = input('Ingese el lado: ');
  display('Cuadrado ')
  Area=numero_dos*numero_dos
  N=pq_exec_params(conn, "INSERT INTO area_figuras (figura, radio_lado1, lado2, area) VALUES('Ccuadrado', $2, 0,$4 );", {numero_dos, numero_dos, numero_tres, Area});
 
  elseif (numero_uno==4)
  printf('\nArea de Rectangulo\n')
  numero_dos = input('Ingese el lado1:');
  numero_tres = input('Ingese la lado2:');
  display('Rectangulo')
  Area=numero_dos*numero_tres
  N=pq_exec_params(conn, "INSERT INTO area_figuras (figura, radio_lado1, lado2, area) VALUES('Rectangul', $2, 0,$4 );", {numero_dos, numero_dos, numero_tres, Area});

  endif