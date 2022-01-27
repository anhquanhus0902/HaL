#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

#define R		2
#define TRUE	1
#define FALSE	0
#define DELAY 	sleep(rand() % R);

void enter_region(int pid);
void leave_region(int pid);

void *reader(void *arg);
void *writer(void *arg);
void readData();
void writeData();

int turn;
int interest[2];

int main(){
	pthread_t r_thread, w_thread;
	
	pthread_create(&r_thread, NULL, reader, NULL);
	pthread_create(&w_thread, NULL, writer, NULL);
	
	pthread_join(r_thread, NULL);
	pthread_join(w_thread, NULL);
	
	return 0;
}

void enter_region(int pid) {
	int oth;
	oth = 1 - pid;
	interest[pid] = TRUE;
	turn = pid;
	while (turn == pid && interest[oth] == TRUE);
}

void leave_region(int pid) {
	interest[pid] = FALSE;
}

void *reader(void *arg){
	int pid = 0;
	while (TRUE){
		enter_region(pid);
		readData();
		leave_region(pid);
		printf("Reader finished reading the data\n");
	}
}

void *writer(void *arg){
	int pid = 1;
	while (TRUE){
		enter_region(pid);
		writeData();
		leave_region(pid);
		printf("Writer finished writing the data\n");
	}
}

void readData(){
	printf("Reader is reading data on the database\n");
	DELAY;
}

void writeData(){
	printf("Writer is writing data to the database\n");
	DELAY;
}
