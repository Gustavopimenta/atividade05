% knowledge_base.pl

% Fatos sobre as pessoas e suas profissões
human(socrates).
human(plato).
human(aristotle).
human(einstein).
human(newton).

profession(socrates, philosopher).
profession(plato, philosopher).
profession(aristotle, philosopher).
profession(einstein, physicist).
profession(newton, physicist).

% Fatos sobre gostos pessoais
likes(socrates, philosophy).
likes(plato, philosophy).
likes(aristotle, philosophy).
likes(einstein, science).
likes(newton, mathematics).

% Relações familiares
parent(socrates, plato).
parent(plato, aristotle).
parent(aristotle, alexander).

% Regras
mortal(X) :- human(X).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
