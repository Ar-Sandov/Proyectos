#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computaci�n aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nA�o bisiesto\n')
numero_uno = input('Ingrese el a�o: ');
  pkg load database
  conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));

if mod(numero_uno, 4) ~= 0
  display('No es bisiesto')
  N=pq_exec_params(conn, "INSERT INTO bisiesto_a�o (_a�o, bisiesto) VALUES($1, 'No');", {numero_uno, numero_uno});

  elseif ((mod(numero_uno, 4) == 0)&&(mod(numero_uno, 100) ~= 0))
  display('Es bisiesto')
  N=pq_exec_params(conn, "INSERT INTO bisiesto_a�o (_a�o, bisiesto) VALUES($1, 'Si');", {numero_uno, numero_uno});

  elseif ((mod(numero_uno, 4) == 0)&&(mod(numero_uno, 100) == 0)&&(mod(numero_uno, 400) ~= 0))
  display('No es bisiesto')
  N=pq_exec_params(conn, "INSERT INTO bisiesto_a�o (_a�o, bisiesto) VALUES($1, 'No');", {numero_uno, numero_uno});

  elseif ((mod(numero_uno, 4) == 0)&&(mod(numero_uno, 100) == 0)&&(mod(numero_uno, 400) == 0))
  display('Es bisiesto')
  N=pq_exec_params(conn, "INSERT INTO bisiesto_a�o (_a�o, bisiesto) VALUES($1, 'Si');", {numero_uno, numero_uno});

else
  display('No se puede calcular')
  endif