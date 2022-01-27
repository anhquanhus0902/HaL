#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
#include<stdlib.h>

#define DELAY	sleep(rand() % 4)

int account;

void *chaGuiTien(){
	int x;
	for (int i = 0; i < 5; ++i){
		x = account;
		DELAY;
		x += 3;
		DELAY;
		account = x;
		DELAY;
		printf("Bo da gui. Account=%d\n", account);
	}
}

void *conRutTien(){
	int y;
	for (int i = 0; i < 5; ++i){
		y = account;
		DELAY;
		y -= 2;
		DELAY;
		if (y >= 0){
			account = y;
			printf("Con ra rut. Account=%d\n", account);
		}
		else{
			printf("Khong du tien\n");
			--i;
		}
		DELAY;
	}
}

int main(){
	pthread_t tid1, tid2;
	printf("Account=%d\n", account);
	pthread_create(&tid1, NULL, chaGuiTien, NULL);
	pthread_create(&tid2, NULL, conRutTien, NULL);
	
	pthread_join(tid1, NULL);
	pthread_join(tid2, NULL);
	return 0;
}
