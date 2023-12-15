/***************
*
* Autores: Alexis Canales y Sergio Hidalgo 
*
* Grupo: 1331
*
****************/

/***************
* EJERCICIO 5 (2p). Procesamiento de sentencias
*
* Si bien un procesamiento completo de lenguaje es una tarea compleja, debido a que
* su uso no siempre es estructurado, podemos utilizar, a base de reglas sencillas, Prolog
* para identificar "frases bien formadas".
* Para ello, se os da una base de conocimiento inicial y se os pide que diseñéis un predicado
* que identifique si una frase es correcta. En el resto del ejercicio iréis ampliando las 
* reglas para identificar frases cada vez más complejas.
*
****************/

% Partimos de la siguiente base de conocimiento simplificada
articulo([X]) :- articulo(X).
articulo(el).
articulo(la).
articulo(un).
articulo(una).

nombre([X]) :- nombre(X).
nombre(perro).
nombre(hueso).

verbo([X]) :- verbo(X).
verbo(come).
verbo(encuentra).

% 1. Define un predicado frase/1 que determine si una frase 
% (codificada como una lista de terminales) es correcta gramaticalmente.
% De momento, nos basta con identificar frases como la siguiente, donde hay un sintagma nominal
% y uno verbal, pero sin complemento de ningún tipo:
% :- frase([el, perro, come]).
% :- frase([la, perro, come]).
% Sin embargo, la siguiente fallaría:
% :- frase([come]). FAIL
% El predicado append/3 puede ser útil para asignar partes de una frase a variables.

sintagmaNominal(N) :- append(X, Y, N), articulo(X), nombre(Y).
sintagmaVerbal(V) :- verbo(V).

frase(F) :- append(N, V, F), sintagmaNominal(N), sintagmaVerbal(V).

% 2. Amplía la base de conocimiento con más hechos (nombres, verbos, determinantes). 
% Al igual que en el ejercicio anterior, no nos vamos a preocupar de la concordancia de género.
% Extiende el predicado anterior y llámalo frase2/1 para que reconozca frases 
% cuyo sintagma verbal tenga uno (o varios) complementos.
% Puedes reutilizar todos los predicados que consideres, pero si tienes que cambiar alguno, 
% renómbralo para mantener la compatibilidad con los ejercicios anteriores.

% no ampliamos más porque si no quedan demasiados como para hacer pruebas

complemento(C) :- nombre(C).
complemento(C) :- sintagmaNominal(C).
complemento(C) :- append(C1, C2, C), complemento(C1), complemento(C2).
sintagmaVerbal2(V2) :- append(V, C, V2), verbo(V), complemento(C).
sintagmaVerbal2(V2) :- verbo(V2).

frase2(F2) :- append(N, V2, F2), sintagmaNominal(N), sintagmaVerbal2(V2).

% 3. Añade adjetivos a la base de conocimiento y crea el predicado frase3/1 que detecte si 
% un nombre va acompañado de un adjetivo. Es decir:
% :- frase3([el, perro, grande, come]).
% De manera opcional, permite la utilización de adjetivos tanto delante como detrás del nombre.

adjetivo([X]) :- adjetivo(X).
adjetivo(limpio).
adjetivo(sucio).
adjetivo(rápido).
adjetivo(lento).

compuesto(C) :- append(X, Y, C), nombre(X), adjetivo(Y).
compuesto(C) :- append(Y, X, C), nombre(X), adjetivo(Y).
sintagmaNominal3(N3) :- append(X, C, N3), articulo(X), compuesto(C).

frase3(F3) :- append(N3, V, F3), sintagmaNominal3(N3), sintagmaVerbal(V).

% 4. Identifica un ejemplo de frase que no lo detecte alguno de tus predicados y explica 
% cuál sería el motivo. Puedes utilizar la lectura declarativa o procedural 
% vista en el ejercicio 1 o apoyarte en trace/0 para tu explicación.

% Un ejemplo de frase no detectada por ninguno de los predicados podría ser "el perro corre rápido"
% ya que en ningún momento hemos hecho que los adjetivos puedan ir separados de un nombre.
% En términos de lectura declarativa: 
% frase/3 --> "Si N y V se concatenan formando F, siendo N un sintagma nominal y V un sintagma verbal, entonces F es una frase"
% frase2/3 --> "Si N y V2 se concatenan formando F2, siendo N un sintagma nominal y V2 un sintagma verbal, entonces F2 es una frase"
% frase3/3 --> "Si N3 y V se concatenan formando F3, siendo N3 un sintagma nominal y V un sintagma verbal, entonces F3 es una frase"
% El único sintagma verbal que acepta complementos es el de frase2/3, en el cual todavía no existía el predicado adjetivo/1 adjetivos.