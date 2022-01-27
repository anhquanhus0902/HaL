all: diskemu.o fs.o makedisk formatdisk createfile deletefile readfile readblock printdir printfat

diskemu.o:	diskemu.c diskemu.h
	gcc -Wall -c diskemu.c

fs.o:	fs.c fs.h diskemu.h
	gcc -Wall -c fs.c

makedisk: makedisk.c diskemu.o
	gcc -Wall -o makedisk makedisk.c diskemu.o

formatdisk: formatdisk.c fs.o diskemu.o
	gcc -Wall -o formatdisk formatdisk.c diskemu.o fs.o

createfile: createfile.c fs.o diskemu.o
	gcc -Wall -o createfile createfile.c diskemu.o fs.o

deletefile: deletefile.c fs.o diskemu.o
	gcc -Wall -o deletefile deletefile.c diskemu.o fs.o

readfile: readfile.c fs.o diskemu.o
	gcc -Wall -o readfile readfile.c diskemu.o fs.o

readblock: readblock.c fs.o diskemu.o
	gcc -Wall -o readblock readblock.c diskemu.o fs.o

printdir: printdir.c fs.o
	gcc -Wall -o printdir printdir.c diskemu.o fs.o

printfat: printfat.c fs.o diskemu.o
	gcc -Wall -o printfat printfat.c diskemu.o fs.o

