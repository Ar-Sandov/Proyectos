#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nComparacion de numeros\n')
numero_uno = input('Ingese el primer numero: ');
numero_dos = input('Ingese el segundo numero: ');
numero_tres = input('Ingese el tercer numero: ');
  pkg load database
  conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));


if ((numero_uno > numero_dos)&&(numero_uno > numero_tres))
  display('El primer numero es mas grande')
  suma=numero_uno+numero_uno+numero_tres
  N=pq_exec_params(conn, "INSERT INTO comparacion_de_numeros (numero1, numero2, numero3, comparacion) VALUES($1, $2, $3, 'El No.1 es mayor');", {numero_uno, numero_dos, numero_tres});

elseif ((numero_dos > numero_uno)&&(numero_dos > numero_tres))
  display('El segundo numero es mas grande')
  printf("%d,%d,%d",numero_uno,numero_uno*2,numero_tres)
  N=pq_exec_params(conn, "INSERT INTO comparacion_de_numeros (numero1, numero2, numero3, comparacion) VALUES($1, $2, $3, 'El No.2 es mayor');", {numero_uno, numero_dos, numero_tres});

elseif ((numero_tres > numero_uno)&&(numero_tres > numero_dos))
  display('El tercer numero es mas grande')
  N=pq_exec_params(conn, "INSERT INTO comparacion_de_numeros (numero1, numero2, numero3, comparacion) VALUES($1, $2, $3, 'El No.3 es mayor');", {numero_uno, numero_dos, numero_tres});

  elseif (numero_dos == numero_uno && numero_dos == numero_tres)
  display('Todos son iguales')
  printf("%d,%d,%d",numero_uno,numero_uno,numero_tres)
  N=pq_exec_params(conn, "INSERT INTO comparacion_de_numeros (numero1, numero2, numero3, comparacion) VALUES($1, $2, $3, 'Los 3 son iguales');", {numero_uno, numero_dos, numero_tres});

elseif (numero_tres == numero_uno)
  display('El segundo numero es diferente')
  N=pq_exec_params(conn, "INSERT INTO comparacion_de_numeros (numero1, numero2, numero3, comparacion) VALUES($1, $2, $3, 'El No.2 es diferente');", {numero_uno, numero_dos, numero_tres});

elseif (numero_dos == numero_uno)
  display('El tercer numero es diferente')
  N=pq_exec_params(conn, "INSERT INTO comparacion_de_numeros (numero1, numero2, numero3, comparacion) VALUES($1, $2, $3, 'El No.3 es diferente');", {numero_uno, numero_dos, numero_tres});

elseif (numero_dos == numero_tres)
  display('El primer numero es diferente')
  N=pq_exec_params(conn, "INSERT INTO comparacion_de_numeros (numero1, numero2, numero3, comparacion) VALUES($1, $2, $3, 'El No.1 es diferente');", {numero_uno, numero_dos, numero_tres});

else
  display('no se puede comparar')
endif