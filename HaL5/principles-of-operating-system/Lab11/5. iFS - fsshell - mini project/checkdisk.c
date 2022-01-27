/* ----------------------------------------------------------------------------------------
	Module checkdisk.c
------------------------------------------------------------------------------------------- */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#ifndef FS_H
#include "fs.h"
#endif

/* Explain in detail your algorithm here
 ...
*/

// gcc -Wall -c diskemu.c && gcc -Wall -c fs.c && gcc -Wall -c checkdisk.c && gcc -Wall -o makedisk makedisk.c diskemu.o && gcc -Wall -o fsshell fsshell.c diskemu.o fs.o

void fs_checkDisk()
{
	printf("Checking disk ...\n");
	// write your code here, add a comment after each line of code

	// Get the number of inodes in the disk
	int numberOfInodes = BLOCKSIZE/sizeof(inode_t);
	printf("Number of inodes: %d\n", numberOfInodes);

	// inode_t inodeTable[numberOfInodes];
	// // Read the inode table into the inodeTable
	// read_block(0, (char*)inodeTable);
}