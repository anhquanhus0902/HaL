/***********************************************************
* The bridge of Vermont
* Starvation prone
***********************************************************/
 
#include<stdio.h>
#include<semaphore.h>
#include<pthread.h>
#include<time.h>
#include <unistd.h>
#include<stdlib.h>
  
#define N 	10
#define up(sem) sem_post(sem)
#define down(sem) sem_wait(sem)
#define DELAY(R) srand(time(NULL));sleep(rand()%R);
  
sem_t bFree;   // 1 if no car is on the bridge
sem_t waitE;   // 0 if east-car waiting
sem_t waitW;   // 0 if west-car waiting

int numE;   // number of east-cars waiting or in bridge
int numW;   // number of west-cars waiting or in bridge


void startE() {  // executed by a east-car to enter bridge
	//...
	down(&waitE);
	++numE;
	if (numE == 1){
		down(&bFree);
	}
	up(&waitE);
}

void endE() {
	//...
	down(&waitE);
	--numE;
	if (numE == 0){
		up(&bFree);
	}
	up(&waitE);
}

void startW() {  // executed by a west-car to enter bridge
	//...
	down(&waitW);
	++numW;
	if (numW == 1){
		down(&bFree);
	}
	up(&waitW);
}

void endW() {
	//...
	down(&waitW);
	--numW;
	if (numW == 0){
		up(&bFree);
	}
	up(&waitW);
}

void* east_car(void* id) {
	int *pI = id;
	DELAY(6);
	printf("East car #%d arrives\n", *pI);
	startE();
	printf("East car #%d crossing\n", *pI);
	sleep(1);
	endE();
	printf("East car #%d exits\n", *pI);
}

void* west_car(void* id) {
	int *pI=id;
	DELAY(6);
	printf("West car #%d arrives\n", *pI);
	startW();
	printf("West car #%d crossing\n", *pI);
	sleep(1);
	endW();
	printf("West car #%d exits\n", *pI);
}

void main() {
	pthread_t threadE_id[N], threadW_id[N];
	int i;
	int car_id[N];
	
	sem_init(&bFree,0,1);
	sem_init(&waitE,0,1);
	sem_init(&waitW,0,1);
	
	for (i=0; i<N; i++) {
		car_id[i]=i;
		pthread_create(&threadE_id[i],NULL,east_car,&car_id[i]);
		// sleep(1);	// take this one out to check for starvation
		pthread_create(&threadW_id[i],NULL,west_car,&car_id[i]);
	}
	
	for (i=0; i<N; i++) {
		pthread_join(threadE_id[i],NULL);
		pthread_join(threadW_id[i],NULL);
	}	
}
