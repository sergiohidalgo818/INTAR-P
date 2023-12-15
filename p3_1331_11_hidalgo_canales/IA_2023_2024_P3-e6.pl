/***************
*
* Autores: Alexis Canales y Sergio Hidalgo 
*
* Grupo: 1331
*
****************/

/***************
* EJERCICIO 6 (1p). Librería clpb
*
* La librería CLP(B) (ver https://www.swi-prolog.org/pldoc/man?section=clpb)
* permite resolver problemas combinatorios con restricciones.
*
* A continuación se os da la solución al siguiente problema resuelto con esta librería:
* Tenemos a 3 sospechosos de un robo, Alice (A), Bob (B) y Carl (C). 
* Al menos uno de ellos es culpable. Condiciones:
* Si A es culpable, tiene exactamente 1 cómplice.
* Si B es culpable, tiene exactamente 2 cómplices.
* ¿Quién es culpable?
*
****************/

:- use_module(library(clpb)).

solve(A,B,C) :-
 % Hay al menos un culpable
 sat(A + B + C),
 % Si A es culpable, tiene exactamente 1 cómplice.
 sat(A =< B # C),
 % Si B es culpable, tiene exactamente 2 cómplices.
 sat(B =< A * C),
 % Asigna valores a las variables de manera que se satisfagan todas las restricciones.
 labeling([A,B,C]).


% 1. Plantea una solución a este problema que sea equivalente a la encontrada por la librería.

resolver(A,B,C) :- member(A, [0, 1]), member(B, [0, 1]), member(C, [0, 1]), A+B+C > 0, (A =:= 1 -> B+C =:= 1; true), (B =:= 1 -> A+C =:= 2; true).

% 2. Discute las ventajas e inconvenientes entre la solución encontrada y el uso de la librería.

% El uso de la librería nos proporciona métodos ya implementados que nos facilitan el trabajo simplificando
% la sintaxis, utilizando operadores similares a los de otros lenguajes y reduciendo el número de predicados
% necesarios en el antecedente.
% Por otro lado, su uso también implica tener que aprender a usarla.

