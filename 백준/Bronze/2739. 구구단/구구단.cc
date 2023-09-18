#include <stdio.h>

int main(void) {
	short n;
	scanf("%hd", &n);
	for (short i = 1; i < 10; i++) {
		printf("%hd * %hd = %hd\n", n, i, n * i);
	}
}