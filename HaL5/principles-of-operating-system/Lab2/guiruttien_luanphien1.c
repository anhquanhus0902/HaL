#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
#include<stdlib.h>

#define DELAY	sleep(rand()%4)

int account, turn;

void *chaGuiTien(){
	int x;
	while (1){
		while (turn != 0);
		x = account;
		DELAY;
		x += 2;
		DELAY;
		account = x;
		DELAY;
		turn = 1;
		printf("Bo da gui. Account=%d\n", account);
	}
}

void *conRutTien(){
	int y;
	while (1){
		while (turn != 1);
		y = account;
		DELAY;
		y -= 3;
		DELAY;
		if (y >= 0){
			account = y;
			printf("Con ra rut. Account=%d\n", account);
		}
		else{
			printf("Khong du tien.\n");
		}
		turn = 0;
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
