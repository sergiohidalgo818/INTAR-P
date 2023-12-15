/***************
*
* Autores: Alexis Canales y Sergio Hidalgo 
*
* Grupo: 1331
*
****************/

/***************
* EJERCICIO 4 (2p). Combate Pokémon
*
* Ash, Misty y Brock van a medir sus fuerzas en combates Pokémon. Para ello,
* Ash cuenta con sus amigos Pikachu, Charmander y Bulbasaur, Misty con sus 
* pokémon de tipo agua Psyduck, Staryu y Starmie y Brock con sus criaturas 
* de tipo roca Geodude, Golem y Onyx. Hemos creado el predicado pokemonOfTrainer/2 
* para relacionar cada pokémon con su entrenador. También hemos construido el 
* predicado pokemonOfType/2 que nos indica el tipo de cada pokémon. Por último, 
* hemos creado el predicado typeWins/2 para introducir la tabla de tipos, 
* que nos indica si un pokémon gana a otro en función de su tipo. 
*
****************/

pokemonOfTrainer(pikachu, ash).
pokemonOfTrainer(charmander, ash).
pokemonOfTrainer(bulbasaur, ash).

pokemonOfTrainer(psyduck, misty).
pokemonOfTrainer(staryu, misty).
pokemonOfTrainer(starmie, misty).

pokemonOfTrainer(geodude, brock).
pokemonOfTrainer(golem, brock).
pokemonOfTrainer(onyx, brock).

pokemonOfType(pikachu, electric).
pokemonOfType(charmander, fire).
pokemonOfType(bulbasaur, grass).
pokemonOfType(psyduck, water).
pokemonOfType(staryu, water).
pokemonOfType(starmie, water).
pokemonOfType(geodude, rock).
pokemonOfType(golem, rock).
pokemonOfType(onyx, rock).

typeWins(water, fire).
typeWins(fire, grass).
typeWins(grass, water).
typeWins(water, rock).
typeWins(rock, fire).
typeWins(grass, rock).
typeWins(electric, water).
typeWins(rock, electric).

% 1) Construye el predicado pokemonWins/2 que indique que un pokémon A gana a 
% un pokémon B si el tipo de A gana al tipo de B.

pokemonWins(A, B) :- pokemonOfType(A, X), pokemonOfType(B, Y), typeWins(X, Y).

% 2) Construye el predicado trainerWins/2 que nos indique que un entrenador A
% gana a un entrenador B si...
% a) El primer pokémon del entrenador A gana al primero del B, el segundo de A
% gana al segundo de B y el tercero de A gana al tercero de B.
% b) Al menos dos pokémon del entrenador A ganan a sus equivalentes del entrenador B. 
% c) Un pokémon del entrenador A es capaz de ganar a los tres del entrenador B. 

trainerWins1(A, B) :- pokemonOfTrainer(X, A), pokemonOfTrainer(Y, A), pokemonOfTrainer(Z, A), pokemonOfTrainer(S, B), pokemonOfTrainer(T, B), pokemonOfTrainer(U, B), pokemonWins(X, S), pokemonWins(Y, T), pokemonWins(Z, U), X\=Y, X\=Z, Y\=Z, S\=T, S\=U, T\=U.

trainerWins2(A, B) :- pokemonOfTrainer(X, A), pokemonOfTrainer(Y, A), pokemonOfTrainer(S, B), pokemonOfTrainer(T, B), pokemonWins(X, S), pokemonWins(Y, T), X\=Y, S\=T.

trainerWins3(A, B) :- pokemonOfTrainer(X, A), pokemonOfTrainer(S, B), pokemonOfTrainer(T, B), pokemonOfTrainer(U, B), pokemonWins(X, S), pokemonWins(X, T), pokemonWins(X, U), S\=T, S\=U, T\=U.

% 3) ¿Quién gana los combates Ash vs Misty, Misty vs Brock y Brock vs Ash
% utilizando los criterios a, b y c?

% trainerWins1(ash, misty). ----> Resultado: false
% trainerWins2(ash, misty). ----> Resultado: true
% trainerWins3(ash, misty). ----> Resultado: true

% trainerWins1(misty, brock). ----> Resultado: true
% trainerWins2(misty, brock). ----> Resultado: true
% trainerWins3(misty, brock). ----> Resultado: true

% trainerWins1(brock, ash). ----> Resultado: false
% trainerWins2(brock, ash). ----> Resultado: true
% trainerWins3(brock, ash). ----> Resultado: false