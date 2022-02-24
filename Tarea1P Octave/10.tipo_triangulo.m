#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf("\nTipo de triangulo\n")

numero_uno = input('Ingese el lado a: ');
numero_dos = input('Ingese el lado b: ');
numero_tres = input('Ingese el lado c: ');
  pkg load database
  conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));


if (numero_uno == numero_dos && numero_uno == numero_tres)
  display('Triangulo Equilatero')
  N=pq_exec_params(conn, "INSERT INTO tipo_triangulo (lado_a, lado_b, lado_c, tipo) VALUES($1, $2, $3,'Equilatero' );", {numero_uno, numero_dos, numero_tres, numero_tres});

  elseif (numero_uno ~= numero_dos && numero_uno ~= numero_tres)
  display('Triangulo Escaleno')
  N=pq_exec_params(conn, "INSERT INTO tipo_triangulo (lado_a, lado_b, lado_c, tipo) VALUES($1, $2, $3,'Escaleno' );", {numero_uno, numero_dos, numero_tres, numero_tres});

  else
  display('Triangulo Isosceles')
  N=pq_exec_params(conn, "INSERT INTO tipo_triangulo (lado_a, lado_b, lado_c, tipo) VALUES($1, $2, $3,'Isosceles' );", {numero_uno, numero_dos, numero_tres, numero_tres});

  
endif