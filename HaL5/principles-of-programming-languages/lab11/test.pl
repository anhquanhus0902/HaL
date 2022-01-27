p(a). %#1
p(b):- !. %#2
p(c). %#3

max(X,Y,X):- X>=Y,!.
max(X,Y,Y):- X<Y.

% cat nhanh xanh
sign(X,-1) :- X<0,!.
sign(X,0) :- X==0,!.
sign(X,1) :- X>0.

% cat nhanh do
sign1(X,-1) :- X<0,!.
sign1(X,0) :- X=<0,!.
sign1(X,1) :- X>0.

sign2(X,-1) :- X<0.
sign2(X,0) :- X=<0.
sign2(X,1) :- X>0.
