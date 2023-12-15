/***************
*
* Autores: Alexis Canales y Sergio Hidalgo 
*
* Grupo: 1331
*
****************/

/***************
* Introducción
*
* Os recomendamos echar un vistazo a la colección de 99 problemas de Prolog publicados en 
* https://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/
* Ahí puedes encontrar una gran serie de problemas con código que te pueden ayudar 
* como entrenamiento.
*
****************/

/***************
* Entrega
*
* Se debe entregar un único fichero comprimido cuyo nombre, todo él en minúsculas y sin acentos, 
* tildes, o caracteres especiales, tendrá la siguiente estructura:
*       p3_gggg_mm_apellido1_apellido2.zip
* Donde gggg es el identificador del grupo y mm es el de la pareja.
* Este fichero debe incluir los ficheros .pl entregados por los profesores con sus correspondientes
* soluciones y descripciones de las mismas como comentarios (no hace falta entregar una memoria por separado).
*
* Recordad utilizar nombres informativos para los términos (hechos, reglas) así como comentar vuestro código 
* adecuadamente para que resulte de fácil lectura.
*
****************/


/***************
* EJERCICIO 1 (1p). Ejercicio de lectura
*
* Escribe la lectura declarativa (para el caso general) 
* y procedural (para la consulta slice([1, 2, 3, 4], 2, 3, L2))
* del predicado slice/4, disponible en
* https://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/p18.pl
*
* Véase https://www.metalevel.at/prolog/reading para un ejemplo.
*
****************/


% Lectura declarativa del caso general (slice([X|_],1,1,[X]).):
% "La partición de una lista [X|_] entre sus índices 1 y 1, ambos incluidos, es [X]"


% Lectura procedural de la consulta slice([1, 2, 3, 4], 2, 3, L2):

% 1. La primera cláusula no aplica porque los valores de los índices no son 1.
% 2. La segunda cláusula no aplica porque el valor del primer índice no es 1.
% 3. La tercera cláusula sí aplica de la siguiente forma: X'=1, Xs'=[2, 3, 4], I'=2, K'=3, Ys'=L2 .

% 4. A continuación, consideramos el objetivo slice([2, 3, 4], 1, 2, L2).

% 5. La primera cláusula no aplica porque los valores de los índices no son 1.
% 6. La segunda cláusula sí aplica de la siguiente forma: X''=2, Xs''=[3, 4], K''=2, Ys'=[X''|Ys''] . Aún hay que comprobar la tercera cláusula.
% 7. La tercera cláusula no aplica porque el valor del primer índice es 1, que no es mayor que 1. Por tanto, volvemos a la segunda cláusula.

% 8. A continuación, consideramos el objetivo slice([3, 4], 1, 1, Ys'').

% 9. La primera cláusula sí aplica de la siguiente forma: X'''=3, X'''=Ys'' . Es el caso base, por lo que esta es la última iteración, aunque aún hay que comprobar la segunda y tercera cláusulas.
% 10. La segunda cláusula no aplica porque el valor del segundo índice es 1, que no es mayor que 1. Aún hay que comprobar la tercera cláusula.
% 11. La tercera cláusula no aplica porque el valor del primer índice es 1, que no es mayor que 1. Por tanto, volvemos a la primera cláusula.

