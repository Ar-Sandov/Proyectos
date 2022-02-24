#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nNumero y sus divisores\n')
numero_uno = input('Ingese el numero: ');
cont=1;
for i=1:numero_uno
    r=mod(numero_uno,i);
    if r==0
      V(cont)=i;
      cont=cont+i;
    endif
end
printf('Los divisores de %i son: \n',numero_uno)
disp(V)
pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
N=pq_exec_params(conn, "INSERT INTO divisores (numero, divisores) VALUES($1, $2);", {numero_uno, V});
