A simple File System (FS) using FAT16
MAT3501 - Principles of Operating System - MIM HUS

Compilation: run 'make'.

Commands:
1) makedisk <power of 2 disk size>
	example: to create a disk of size 2^20B = 1MB, run "makedisk 20"
2) formatdisk
	format the disk with empty root dir and empty fat table
3) createfile <sourcefile>
	create a sfs file from <sourcefile>
3) reafile <sfs file name>
	read content of a file in sfs
4) deletefile <sfs file name>
	delete a file in sfs
5) readblock <block number>
	read content of a sfs disk block
6) printfat
	print FAT table
7) printdir
	print content of the root directory