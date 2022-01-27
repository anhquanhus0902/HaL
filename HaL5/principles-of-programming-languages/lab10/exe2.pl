thick(bear).            /*#1*/
thick(elephant).        /*#2*/
small(cat).             /*#3*/
brown(bear).            /*#4*/
grey(elephant).         /*#5*/
black(cat).             /*#6*/
dark(Z) :- black(Z).    /*#7*/
dark(Z) :- brown(Z).    /*#8*/