#TAREA PREPARATORIA PRIMER PARCIAL
#Proyectos de computación aplicados a IE
#Arlin Emanuel Sandoval Barrios 2005112176
printf('\nCantidad de vocales\n')
entrada=input("Ingrese la palabra: ","s");
v=['a','e','i','o','u'];
n=[];
for i=1:5
  n=[n strfind(entrada,v(i))];
end
cantidad_vocales=length(n);
display(cantidad_vocales)
pkg load database
conn = pq_connect (setdbopts ("dbname", "Calculadora", "host", "localhost", "port", "5432", "user", "postgres", "password", "a123b"));
N=pq_exec_params(conn, "INSERT INTO contar_vocales (palabra, vocales) VALUES($1, $2);", {entrada, cantidad_vocales});
