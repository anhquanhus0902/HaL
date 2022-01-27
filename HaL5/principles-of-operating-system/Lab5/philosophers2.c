// Dining philosophers with think() and eat(), visualized.
 
#include<stdio.h>
#include<semaphore.h>
#include<pthread.h>
#include<unistd.h>
#include <stdlib.h>
  
#define N 5
#define THINKING 0
#define HUNGRY 1
#define EATING 2
#define LEFT (i+N-1)%N
#define RIGHT (i+1)%N
#define R 3
#define up(sem) sem_post(sem)
#define down(sem) sem_wait(sem)
#define DELAY	sleep(rand() % 4)
  
sem_t mutex;
sem_t S[N];
  
void * philosopher(void *num);
void take_chopsticks(int);
void put_chopsticks(int);
void test(int);
void think(int);
void eat(int);
void print_philosophers(void);
  
int state[N];
int phil_num[N];
  
int main()
{
    int i;
    pthread_t thread_id[N];
    sem_init(&mutex,0,1);
    for(i=0;i<N;i++)
        sem_init(&S[i],0,0);
    for(i=0;i<N;i++)
    {
		phil_num[i]=i;
        pthread_create(&thread_id[i],NULL,philosopher,&phil_num[i]);
    }
    for(i=0;i<N;i++)
        pthread_join(thread_id[i],NULL);
}
  
void *philosopher(void *num)
{
	int i=*(int*)num;
	while(1)
    {
        think(i);
        take_chopsticks(i);
        eat(i);
        put_chopsticks(i);
    }
}
  
void take_chopsticks(int i)
{
    down(&mutex);
    state[i] = HUNGRY;
	print_philosophers();
    test(i);
    up(&mutex);
    down(&S[i]);
    sleep(1);
}
  
void test(int i)
{
    if (state[i] == HUNGRY && state[LEFT] != EATING && state[RIGHT] != EATING)
    {
        state[i] = EATING;
        sleep(2);
        up(&S[i]);
    }
}
  
void put_chopsticks(int i)
{
    down(&mutex);
    state[i] = THINKING;
    test(LEFT);
    test(RIGHT);
    up(&mutex);
}

void think(int i) {
	down(&mutex);
	print_philosophers();
	up(&mutex);
	DELAY;
}

void eat(int i) {
	down(&mutex);
	print_philosophers();
	up(&mutex);
	DELAY;
}

void print_philosophers(void) {
	int i;
	char ch;
	for (i=0; i<N; i++) {
		if (state[i]==0) ch='T'; else
			if (state[i]==1) ch='H'; else ch='E';
		printf("%c ", ch);
	}
	printf("\n");
}