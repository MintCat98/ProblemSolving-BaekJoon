#include <stdio.h>

int main(void) {
	short n;
	scanf("%hd", &n);
	short a = n / 4;
	short b = n % 4;
	for (short i = 0; i < a; i++) {
		printf("long ");
	}
	if (b != 0) {
		printf("long ");
	}
	printf("int");
}