#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
#include<stdlib.h>

#define DELAY	sleep(rand()%4)

int account, turn;

void *chaGuiTien(void* tienGui){
	int x, soTienGui;
	soTienGui = (int) tienGui;
	while (1){
		while (turn != 0);
		x = account;
		soTienGui = (int) tienGui;
		DELAY;
		x += soTienGui;
		DELAY;
		account = x;
		DELAY;
		turn = 1;
		printf("Bo da gui. Account=%d\n", account);
	}
}

void *conRutTien(void* tienRut){
	int y, soTienRut;
	while (1){
		while (turn != 1);
		y = account;
		soTienRut = (int) tienRut;
		DELAY;
		y -= soTienRut;
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
	int tienGui = 2, tienRut = 3;
	printf("Account=%d\n", account);
	pthread_create(&tid1, NULL, chaGuiTien, (void*) tienGui);
	pthread_create(&tid2, NULL, conRutTien, (void*) tienRut);
	
	pthread_join(tid1, NULL);
	pthread_join(tid2, NULL);
	return 0;
}
