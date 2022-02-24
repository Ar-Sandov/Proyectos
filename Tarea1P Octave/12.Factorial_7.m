#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nFactorial, si es divisible entre 7\n')
numero_uno = input('Ingese el numero: ');
fact=1;
if mod(numero_uno, 7) == 0
  display('Si es divisible entre 7')
  for i=numero_uno:-1:1
    fact=fact*i;
  endfor
  fprintf("El factorial de %d es %f \n",numero_uno,fact)
  pkg load database
  conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
  N=pq_exec_params(conn, "INSERT INTO factorial_7 (numero, factorial) VALUES($1, $2);", {numero_uno, fact});

else
  display('No es divisible entre 7')
  endif