#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>
#include<semaphore.h>

#define up(sem) 				sem_post(sem)
#define down(sem)				sem_wait(sem)
#define DELAY					sleep(rand() % 4)
#define N						20

sem_t mutex, full;
int visitorsInCave = 0, maxVisitorsInCave = 5;
int visitor_num[N];

void *visitor(void* arg);
void take_ticket(int);
void enter_cave(int);
void enjoy(int);
void leave_cave(int);
void go_home(int);

void *visitor(void* vsNum){
	int i = *((int*) vsNum);
	down(&full);
	take_ticket(i);
	++visitorsInCave;
	printf("There are %d visitors in the cave\n", visitorsInCave);
	
	down(&mutex);
	enter_cave(i);
	DELAY;
	up(&mutex);
	enjoy(i);
	DELAY;
	down(&mutex);
	leave_cave(i);
	--visitorsInCave;
	DELAY;
	up(&mutex);
	up(&full);
	go_home(i);
}

void take_ticket(int i){
	printf("Visitor %d is taking the ticket\n", i);
	
}

void enter_cave(int i){
	printf("Visitor %d is entering the cave\n", i);
}

void enjoy(int i){
	printf("Visitor %d: yahoo, yahoo, hooya, yahoo\n", i);
	printf("Still visitor %d: hang MU đẹp quá, MU là vô đối\n", i);
}

void leave_cave(int i){
	printf("Visitor %d is leaving the cave\n", i);
}

void go_home(int i){
	printf("Visitor %d is going home\n", i);
}

int main(){
	sem_init(&mutex, 0, 1);
	sem_init(&full, 0, N);
	pthread_t thread_id[N];
	for (int i = 0; i < N; ++i){
		visitor_num[i] = i;
		pthread_create(&thread_id[i], NULL, visitor, &visitor_num[i]);
	}
	for (int i = 0; i < N; ++i){
		pthread_join(thread_id[i], NULL);
	}
	return 0;
}