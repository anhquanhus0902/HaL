#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>

#define N			5	
#define LEFT(i)		(i-1)%N
#define RIGHT(i)	(i+1)%N
#define THINKING	0
#define HUNGRY		1
#define EATING		2

int state[N];
