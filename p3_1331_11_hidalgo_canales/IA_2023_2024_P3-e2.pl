/***************
*
* Autores: Alexis Canales y Sergio Hidalgo 
*
* Grupo: 1331
*
****************/

/***************
* EJERCICIO 2 (2p). Casa Stark
*
* Construir un árbol genealógico con Prolog es fácil. Basta con crear 
* un predicado parent\2 para indicar que una persona es padre o madre de otra 
* y así construir de generación en generación. Aquí hemos creado 
* la casa Stark de Juego de tronos. 
*
****************/

parent(eddard, robb).
parent(eddard, bran).
parent(eddard, rickon).
parent(eddard, sansa).
parent(eddard, arya).
parent(catelyn, robb).
parent(catelyn, bran).
parent(catelyn, rickon).
parent(catelyn, sansa).
parent(catelyn, arya).

parent(rickard, eddard).
parent(rickard, brandon).
parent(rickard, benjen).
parent(rickard, lyanna).
parent(lyarra, eddard).
parent(lyarra, brandon).
parent(lyarra, benjen).
parent(lyarra, lyanna).

male(rickard).
male(brandon).
male(eddard).
male(benjen).
male(robb).
male(bran).
male(rickon).

female(lyarra).
female(lyanna).
female(catelyn).
female(sansa).
female(arya).

% 1) Empleando el predicado parent, construye los siguientes métodos:
% father(M, N), que devuelva True si M es el padre de N.
% mother(M, N), que devuelva True si M es la madre de N.
% son(M, N), que devuelva True si M es el hijo de N.
% daugther(M, N), que devuelva True si M es la hija de N.

% father(M, N), que devuelva True si M es el padre de N.
father(M, N) :- parent(M, N), male(M).
% mother(M, N), que devuelva True si M es la madre de N.
mother(M, N) :- parent(M, N), female(M).
% son(M, N), que devuelva True si M es el hijo de N.
son(M, N) :- parent(N, M), male(M).
% daugther(M, N), que devuelva True si M es la hija de N.
daughter(M, N) :- parent(N, M), female(M).

% 2) Construye los métodos grandparent, grandfather y grandmother 
% que permitan encontrar los abuelos de un Stark, así como los métodos
% grandson y grandaugther que devuelvan los nietos y nietas de un Stark.

% grandparent(M, N), que devuelva True si M es abuelo o abuela de N.
grandparent(M, N) :- parent(M, L), parent(L, N).
% grandfather(M, N), que devuelva True si M es el abuelo de N.
grandfather(M, N) :- grandparent(M, N), male(M).
% grandmother(M, N), que devuelva True si M es la abuela de N.
grandmother(M, N) :- grandparent(M, N), female(M).
% grandson(M, N), que devuelva True si M es el nieto de N.
grandson(M, N) :- grandparent(N, M), male(M).
% granddaughter(M, N), que devuelva True si M es la nieta de N.
granddaughter(M, N) :- grandparent(N, M), female(M).

% 3) ¿Cómo crearías los métodos de hermano (brother), hermana (sister),
% tío (uncle), tía (aunt), sobrino (nephew) y sobrina (niece).

% sibling(M, N), que devuelva True si M es hermano o hermana de N.
sibling(M, N) :- father(L, M), father(L, N), mother(J, M), mother(J, N), M\=N.
% brother(M, N), que devuelva True si M es el hermano de N.
brother(M, N) :- sibling(M, N), male(M).
% sister(M, N), que devuelva True si M es la hermana de N.
sister(M, N) :- sibling(M, N), female(M).
% uncle(M, N), que devuelva True si M es el tío de N.
uncle(M, N) :- parent(L, N), sibling(M, L), male(M).
% aunt(M, N), que devuelva True si M es la tía de N.
aunt(M, N) :- parent(L, N), sibling(M, L), female(M).
% nephew(M, N), que devuelva True si M es el sobrino de N.
nephew(M, N) :- parent(L, M), sibling(N, L), male(M).
% niece(M, N), que devuelva True si M es la sobrina de N.
niece(M, N) :- parent(L, M), sibling(N, L), female(M).