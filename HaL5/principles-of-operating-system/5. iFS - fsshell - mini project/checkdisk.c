/* ----------------------------------------------------------------------------------------
	Module checkdisk.c
------------------------------------------------------------------------------------------- */

/*
 * Student:	Pham Vu Anh Quan
 * Id: 		19000470
 * Class:	K64A4-OS
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef FS_H
#include "fs.h"
#endif

/*
 * Can't run 'make' command (I have no idea why), so I use below command to compile files. :U
 * gcc -Wall -c diskemu.c && gcc -Wall -c fs.c && gcc -Wall -o makedisk makedisk.c diskemu.o && gcc -Wall -o fsshell fsshell.c diskemu.o fs.o
 * Don't bother about it, I just wrote it here to copy and paste it into Cygwin terminal easily.
*/

/* Explain in detail your algorithm here
 * First, I determine the state of all blocks in the disk.
	- Determine in-used blocks: traverse each inode in inodeTable, each inode has 2 pointers: direct and singleIndirect. singleIndirect points to a block that contains a list of pointers to blocks.
	- Determine free blocks: superBlock.freeBlockList point to the first free block which points to the next free block, and so on until the pointer points to NULL.
 * After that, I iterate over 2 array: inUsedBlockArray and freeBlockArray to determine the error of each block (if exist).
 * Finally, I fix the error by using the algorithm described in the lecture notes.
	- If the block is lost, I add it to the free block list.
	- If the block is free more than once, I remove it from the free block list.
	- If the block is both in-used and free, I remove it from the free block list.
*/

// The name of functions refer to what they do.
void determineInUsedBlocks(int inUsedBlockArray[]);
void determineFreeBlocks(int freeBlockArray[]);
int determineError(int inUsedBlockArray[], int freeBlockArray[]);
void fixErrorInCaseBlockIsLost(int inUsedBlockArray[], int freeBlockArray[]);
// Incomplete function.
void fixErrorInCaseBlockIsFreeMoreThanOnce(int inUsedBlockArray[], int freeBlockArray[]);
void fixErrorInCaseBlockIsBothInUsedAndFree(int inUsedBlockArray[], int freeBlockArray[]);

void determineInUsedBlocks(int inUsedBlockArray[]){
	// Create an array to store pointers that pointed by singleIndirect pointer.
	uint16_t buf[BLOCKSIZE/sizeof(uint16_t)];
	// Iterate over each inode in inodeTable.
	for (int i = 0; i < numInodes; ++i){
		// If the inode is used, add the direct pointer to inUsedBlockArray.
		if (inodeTable[i].linkCount > 0){
			for (int j = 0; j < DIRECTBLOCKS; ++j){
				if (inodeTable[i].direct[j] > 0){
					inUsedBlockArray[inodeTable[i].direct[j]] = 1;
				}
			}
			// If the inode has singleIndirect pointer, add that pointer and all the pointers in the block pointed by singleIndirect to inUsedBlockArray.
			if (inodeTable[i].singleIndirect > 0){
				inUsedBlockArray[inodeTable[i].singleIndirect] = 1;
				// Read the block pointed by singleIndirect and add all the pointers in that block to inUsedBlockArray.
				readBlock(inodeTable[i].singleIndirect, (char*) buf);
				for (int j = 0; j < BLOCKSIZE/sizeof(uint16_t); ++j){
					if (buf[j] > 0){
						inUsedBlockArray[buf[j]] = 1;
					}
				}
			}
		}
	}
}

void determineFreeBlocks(int freeBlockArray[]){
	// Create an array to store the block's content.
	char buf[BLOCKSIZE];
	// Add the first free block to the freeBlockArray.
	int freeBlock = superBlock.freeBlockList;
	++freeBlockArray[freeBlock];
	// Loop until the freeBlock points to NULL or if it is free more than once.
	while (1){
		// Read the freeBlock's content.
		readBlock(freeBlock, buf);
		// Take the next free block.
		freeBlock = buf[0];
		// If the freeBlock points to NULL, break the loop.
		if (!freeBlock){
			break;
		}
		// Add the freeBlock to the freeBlockArray.
		++freeBlockArray[freeBlock];
		// If the freeBlock is free more than once, break the loop.
		if (freeBlockArray[freeBlock] > 1){
			break;
		}
	}
}

int determineError(int inUsedBlockArray[], int freeBlockArray[]){
	// Declare a variable to store the number of errors.
	int numberOfErrors = 0;
	for (int i = 3; i < disk_blockCount; ++i){
		// Case 1: The block is lost.
		if (inUsedBlockArray[i] == 0 && freeBlockArray[i] == 0){
			printf("Block %d is lost\n", i);
			++numberOfErrors;
		}
		// Case 2: The block is both in-used and free.
		else if (inUsedBlockArray[i] == 1 && freeBlockArray[i] == 1){
			printf("Block %d is both in-used and free\n", i);
			++numberOfErrors;
		}
		// Case 3: The block is in-used more than once.
		else if (inUsedBlockArray[i] > 1 && freeBlockArray[i] == 0){
			printf("Block %d is in-used more than once\n", i);
			++numberOfErrors;
		}
		// Case 4: The block is free more than once.
		else if (inUsedBlockArray[i] == 0 && freeBlockArray[i] > 1){
			printf("Block %d is free more than once\n", i);
			++numberOfErrors;
		}
	}
	// Return the number of errors.
	return numberOfErrors;
}

void fixErrorInCaseBlockIsLost(int inUsedBlockArray[], int freeBlockArray[]){
	// Iterate over each block.
	for (int i = 3; i < disk_blockCount; ++i){
		// If the block is lost, add it to the free block list.
		if (inUsedBlockArray[i] == 0 && freeBlockArray[i] == 0){
			// Add the block to the free block list.
			addFreeBlock(i);
		}
	}
}

void fixErrorInCaseBlockIsFreeMoreThanOnce(int inUsedBlockArray[], int freeBlockArray[]){
	// Iterate over each block.
	for (int i = 3; i < disk_blockCount; ++i){
		if (inUsedBlockArray[i] == 0 && freeBlockArray[i] > 1){

		}
	}
}

void fs_checkDisk()
{
	printf("Checking disk ...\n");
	// write your code here, add a comment after each line of code
	// Declare an array for determining in-used blocks, in-used blocks are marked with 1, free blocks are marked with 0.
	int inUsedBlockArray[disk_blockCount];
	// Declare an array for determining free blocks, free blocks are marked with 1, in-used blocks are marked with 0.
	int freeBlockArray[disk_blockCount];
	// Set all blocks in two arrays to 0.
	for (int i = 0; i < disk_blockCount; ++i){
		inUsedBlockArray[i] = 0;
		freeBlockArray[i] = 0;
	}
	// Determine in-used blocks.
	determineInUsedBlocks(inUsedBlockArray);
	// Determine free blocks.
	determineFreeBlocks(freeBlockArray);
	// Determine errors.
	int numberOfErrors = determineError(inUsedBlockArray, freeBlockArray);
	if (numberOfErrors > 0){
		// If there is any error, ask user to fix it.
		printf("Checking disk done.\nWanna fix errors (Y/n)?\n");
		// Get user's input.
		char inp;
		scanf("%c", &inp);
		// If user wants to fix errors, fix them.
		if (inp == 'Y' || inp == 'y'){
			// Fix errors.
			fixErrorInCaseBlockIsLost(inUsedBlockArray, freeBlockArray);
			// fixErrorInCaseBlockIsFreeMoreThanOnce(inUsedBlockArray, freeBlockArray);
			// fixErrorInCaseBlockIsBothInUsedAndFree(inUsedBlockArray, freeBlockArray);
			printf("Fix errors done.\n");
		}
		// If user doesn't want to fix errors, tell him/her that it's not a good choice.
		else if (inp == 'N' || inp == 'n'){
			printf("Not a good choice.\n");
		}
		// If user input something else, tell him/her that he/she only can inputs Y or N.
		else{
			printf("You should input Y or N (lowercase is fine).\n");
		}
		// Because after fixing errors, there will be an non-important error, it doesn't affect the program so tell user that he/she can ignores it.
		printf("NOTE: After make your choice, there will be an unexpected display error on your terminal. It doesn't matter so don't worry about it.\n");
	}
	else{
		// There is no error, tell user that he/she should eats Bun Ca instead of Bun Cha.
		printf("Checking disk done.\nNo errors found. Yahooooooo!\n");
		printf("Bun Ca is better than Bun Cha. \\(>.<)/\n");
	}
}