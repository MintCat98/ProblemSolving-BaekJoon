#include <stdio.h>

int main(void) {
	short t;
	scanf("%hd", &t);
	for (short i = 0; i < t; i++) {
		short a, b;
		scanf("%hd%hd", &a, &b);
		printf("%hd\n", a + b);
	}
}