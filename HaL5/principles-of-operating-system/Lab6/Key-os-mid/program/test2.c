#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

void main(){
	if (fork()){
		printf("A");
	}
	else{
		fork();
		fork();
		printf("B");
	}
	printf("C");
}
