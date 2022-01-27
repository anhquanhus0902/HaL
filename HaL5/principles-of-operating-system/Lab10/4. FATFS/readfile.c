/* ----------------------------------------------------------------------------------------
	Read content of an FS file.
	Course: MAT3501 - Principles of Operating System, MIM - HUS
	Summary: Use FS file functions to read content of a given file name.
------------------------------------------------------------------------------------------- */

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


#include "fs.h"

int main(int argc, char *argv[])
{
	char diskname[128]; 
	char filename[128]; 
	unsigned char buf[BLOCKSIZE];
	int fs_fd, n, i, size; 
		
	if (argc != 2) {
		printf ("usage: %s <filename>\n", argv[0]); 
		exit (-1);
	}
	
       
	strcpy (diskname, DISKNAME);
	strcpy (filename, argv[1]);
		
	if (fs_mount (diskname) != 0) {
		printf ("Could not mount disk %s\n", diskname); 
		exit (-2); 
	}
	//else printf ("Filesystem %s mounted\n", diskname); 

	// read file content
	fs_fd = fs_open(filename);
	if (fs_fd<0) { fprintf(stderr,"Cannot open file\n"); return(-3);}
	size = fs_fileSize(fs_fd);
	
	while (size>=BLOCKSIZE) {
		n = fs_read(fs_fd, buf, BLOCKSIZE); 
		size -= BLOCKSIZE;
		for (i=0; i<n; i++) printf("%c", buf[i]);
	}
	n = fs_read(fs_fd, buf, size); 
	for (i=0; i<n; i++) printf("%c", buf[i]);
	printf("\n");
		
	fs_close(fs_fd);
	
	
	fs_umount(); 
	//printf ("Filesystem %s unmounted\n", diskname);

	return (0);		
}
