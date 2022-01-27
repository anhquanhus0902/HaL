path(G,A,B,P) :- path1(G,A,[B],P).
path1(_,A,[A|Tail],[A|Tail]).
path1(G,A,[Y|Tail],P) :- adj(G,X,Y), \+member(X,[Y|Tail]), path1(G,A,[X,Y|Tail],P).
adj(graph(_,Es),X,Y) :- member(edge(X,Y),Es); member(edge(Y,X),Es).