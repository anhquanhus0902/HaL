parent(hung,nam).
parent(hung,nga).
parent(hung,tuan).
parent(nam,cuong).
parent(nam,linh).
parent(cuong,hai).
parent(nga,long).
parent(nga,minh).
woman(nga).
woman(linh).
man(hung).
man(tuan).
man(nam).
man(cuong).
man(hai).
man(long).
man(minh).

grandparent(X,Y):-parent(X,Z),parent(Z,Y).
mom(X,Y):-parent(X,Y), woman(X).
sibling(X,Y):-parent(Z,X),parent(Z,Y),X\=Y.