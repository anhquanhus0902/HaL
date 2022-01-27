#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

#define N 		5
#define R		4
#define TRUE	1
#define FALSE	0

void enter_region(int pid);
void leave_region(int pid);

void* producer(void *arg);
void* consumer(void *arg);
void produce_item(int* pItem);
void enter_item(int item);
void get_item(int* pItem);
void consume_item(int item);

int turn;
int idx;
int interest[2];
int queue[N];

int main() {
	pthread_t p_thread, c_thread;
	
	pthread_create(&p_thread, NULL, producer, NULL);
	pthread_create(&c_thread, NULL, consumer, NULL);
	
	pthread_join(p_thread, NULL);
	pthread_join(c_thread, NULL);
	
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

void* producer(void *arg) {
	int item;
	printf("P: Hello\n");
	while(TRUE) {
		produce_item(&item);
		enter_region(0);
		enter_item(item);
		leave_region(0);
		sleep(rand() % R);
    }
	return NULL;
}

void* consumer(void *arg) {
	int item;
	printf("C: Hello\n");
	while(TRUE) {
		enter_region(1);
		get_item(&item);
		consume_item(item);
		leave_region(1);
		sleep(rand() % R);
	}
	return NULL;
}

void produce_item(int* pItem) {
	(*pItem) = rand() % 100;
	printf("P: Produce item %d\n", *pItem);
}

void enter_item(int item) {
	queue[idx] = item;
	++idx;
	printf("P: Enter item %d\n", item);
	if (idx >= N){
		printf("P: The queue is full\n");
	}
}

void get_item(int* pItem) {
	--idx;
	(*pItem) = queue[idx];
	printf("C: Get item %d\n", *pItem);
	if (idx == 0){
		printf("C: The queue is empty\n");
	}
}

void consume_item(int item) {
	printf("C: Item %d is yum yum!\n", item);
}
