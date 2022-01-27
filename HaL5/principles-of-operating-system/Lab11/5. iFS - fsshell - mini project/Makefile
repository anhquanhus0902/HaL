all: diskemu.o fs.o makedisk fsshell

diskemu.o:	diskemu.c diskemu.h
	gcc -Wall -c diskemu.c

sfs.o:	fs.c fs.h diskemu.h
	gcc -Wall -c fs.c

checkdisk.o:	checkdisk.c checkdisk.h fs.h
	gcc -Wall -c checkdisk.c


makedisk: makedisk.c diskemu.o
	gcc -Wall -o makedisk makedisk.c diskemu.o

fsshell: fsshell.c fs.o diskemu.o
	gcc -Wall -o fsshell fsshell.c diskemu.o fs.o
