//producer consumer using concurrent processes
// gcc -pthread -lrt

#include <stdio.h>             
#include <sys/mman.h>
#include <semaphore.h>
#include <sys/fcntl.h>
#include <assert.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

#define N 2
#define R 4
#define TRUE 1
#define up(sem) sem_post(sem)
#define down(sem) sem_wait(sem)

void producer(void);
void consumer(void);
void produce_item(int* pItem);
void enter_item(int item);
void get_item(int* pItem);
void consume_item(int item);

// shared memory
struct mySharedMem {
	sem_t full,empty,mutex;
	int queue[N];
	int idx;
	int start;
} *pMem;

int main() {
	pid_t pid,cid;
	int shmfd;
	int status;
		
	// Create unsized shared memory object;
	shmfd = shm_open ("mySharedMemObject", O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
	assert (shmfd != -1);
	
	// Resize the region to store 1 struct instance
	assert (ftruncate (shmfd, sizeof (struct mySharedMem)) != -1);
	
	// Map the object into memory so file operations aren't needed
	pMem = mmap (NULL, sizeof (struct mySharedMem),PROT_READ | PROT_WRITE, MAP_SHARED, shmfd, 0);
	assert (pMem != MAP_FAILED);
	
	// Initialize shared data, done only by the 1st arriver
	if (pMem->start==0) {
		sem_init(&(pMem->mutex),1,1);
		sem_init(&(pMem->empty),1,N);
		sem_init(&(pMem->full),1,0);
		pMem->idx = 0;
		pMem->start=1;
		printf("Press enter to continue\n");
		getchar();
	}
	consumer();
	munmap (pMem, sizeof (struct mySharedMem)); // unmap the object
	shm_unlink ("mySharedMemObject");	// remove the object
	return 0;
}

void consumer() {
	int i, item;
	printf("C: Hello\n");
	for (i=0; i<10; i++) {
		down(&(pMem->full));
		down(&(pMem->mutex));
		get_item(&item);
		up(&(pMem->empty));
		up(&(pMem->mutex));
		
		consume_item(item);
		sleep(rand() % R);
	}
}

void get_item(int* pItem) {
	pMem->idx--;
	(*pItem)=pMem->queue[pMem->idx];
	printf("C: Get item %d\n", *pItem);
	if (pMem->idx==0) printf("C: The queue is empty\n");
}

void consume_item(int item) {
	printf("C: Item %d is yum yum!\n", item);
}