#include<stdio.h>
#include<pthread.h>

char *pHello = "Hello World";

void *myThread(void* pStr){
	printf("%s\n", (char*) pStr);
}

int main(){
	pthread_t tid;
	pthread_create(&tid, NULL, myThread, (void*) pHello);
	pthread_join(tid, NULL);
	return 0;
}
