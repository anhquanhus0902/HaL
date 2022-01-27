//producer consumer using concurrent threads

#include<stdio.h>             
#include<pthread.h>
#include<semaphore.h>

#define N 5
#define R 4
#define TRUE 1
#define up(sem) sem_post(sem)
#define down(sem) sem_wait(sem)

void* producer(void *arg);
void* consumer(void *arg);
void produce_item(int* pItem);
void enter_item(int item);
void get_item(int* pItem);
void consume_item(int item);

sem_t full,empty,mutex;
int queue[N];
int idx;

int main() {
	pthread_t pid,cid;

	sem_init(&mutex,0,1);
	sem_init(&empty,0,N);
	sem_init(&full,0,0);

	pthread_create(&pid,NULL,producer,NULL);
	pthread_create(&cid,NULL,consumer,NULL);
	pthread_join(pid,NULL);
	pthread_join(cid,NULL);
}

void* producer(void*arg) {
	int item;
	printf("P: Hello\n");
	while(TRUE) {
		produce_item(&item);
		down(&empty);		
		down(&mutex);
		enter_item(item);
		up(&full);
		up(&mutex);	
		sleep(rand()% R);
    }
	return NULL;
}

void* consumer(void *arg) {
	int item;
	printf("C: Hello\n");
	while(TRUE) {
		down(&full);		
		down(&mutex);
		get_item(&item);
		up(&empty);
		consume_item(item);
		up(&mutex);
		sleep(rand()% R);
	}
	return NULL;
}

void produce_item(int* pItem) {
	(*pItem)=rand() % 100; // generate a random integer upto 99
	printf("P: Produce item %d\n", *pItem);
}

void enter_item(int item) {
	queue[idx]=item;
	idx++;
	printf("P: Enter item %d\n", item);
	if (idx>=N) printf("P: The queue is full\n");
}

void get_item(int* pItem) {
	idx--;
	(*pItem)=queue[idx];
	printf("C: Get item %d\n", *pItem);
	if (idx==0) printf("C: The queue is empty\n");
}

void consume_item(int item) {
	printf("C: Item %d is yum yum!\n", item);
}
