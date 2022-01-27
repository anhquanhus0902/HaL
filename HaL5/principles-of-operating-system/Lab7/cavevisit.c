//prehistoric cave visitors

#include<stdio.h>             
#include<pthread.h>
#include<semaphore.h>
#include<unistd.h>
#include<stdlib.h>

#define N 5		// Max visitors in the cave
#define MAXTHREADS 20
#define TRUE 1
#define FALSE 0
#define up(sem) sem_post(sem)
#define down(sem) sem_wait(sem)
#define R 4
#define DELAY(R)	sleep(rand() % R);

sem_t visitors, mutex;
int noOfVisitors;

void* caveVisitor(void* id) {
	int i = *((int*) id);
	// Getting a ticket
	down(&visitors);
	++noOfVisitors;
	printf("There are %d visitors in the cave\n", i);
	// Entering the cave through a 1 man passage
	down(&mutex);
	printf("Visitors %d is entering the cave\n", i);
	up(&mutex);
	printf("Visitors %d is now in the cave", i);
	// Contemplating
	printf("Visitors %d is contemplating", i);
	DELAY(2);
	// Getting out through the 1 man passage
	down(&mutex);
	printf("Visitors %d is leaving the cave\n", i);
	up(&mutex);
	printf("Visitors %d is now out the cave", i);
	// Going home
	up(&visitors);
}

int main() {
	pthread_t tid[MAXTHREADS];
	int visitorID[MAXTHREADS];
	int i;

	sem_init(&mutex,0,1);
	sem_init(&visitors,0,N);
	
	for (i=0; i<MAXTHREADS; i++) {
		visitorID[i]=i+1;
		pthread_create(&tid[i],NULL,caveVisitor,&visitorID[i]);
		sleep(rand() % (R));
	}
	for (i=0; i<MAXTHREADS; i++) {
		pthread_join(tid[i],NULL);
	}
}

