height_person(nam,1.73).
height_person(hung,1.86).
height_person(nga,1.56).
height_person(linh,1.61).
taller_person(X,Y):-height_person(X,HX),height_person(Y,HY),HX>HY.