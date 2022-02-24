#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nClasificacion de taxis\n')
numero_uno = input('Ingrese el modelo: ');
numero_dos = input('Ingrese el kilometraje: ');
pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));

if numero_uno<2007 && numero_dos>20000
  display('El taxi debe renovarse')
  N=pq_exec_params(conn, "INSERT INTO taxis (modelo, kilometraje, condicion) VALUES($1,$2, 'Renovar');", {numero_uno, numero_dos, numero_dos});

  elseif (numero_uno>=2007 && numero_uno<=2013 && numero_dos<20000)
  display('El taxi debe recibir mantenimiento')
  N=pq_exec_params(conn, "INSERT INTO taxis (modelo, kilometraje, condicion) VALUES($1,$2, 'Mantenimiento');", {numero_uno, numero_dos, numero_dos});

  elseif numero_uno>2013 && numero_dos<10000
  display('El taxi esta en optimas condiciones')
  N=pq_exec_params(conn, "INSERT INTO taxis (modelo, kilometraje, condicion) VALUES($1,$2, 'Renovar');", {numero_uno, numero_dos, numero_dos});

  else
  display('Mecanico')
  N=pq_exec_params(conn, "INSERT INTO taxis (modelo, kilometraje, condicion) VALUES($1,$2, 'Mecanico');", {numero_uno, numero_dos, numero_dos});

  endif