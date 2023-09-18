#include <stdio.h>

int main(void) {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		short a, b;
		scanf("%hd%hd", &a, &b);
		printf("%hd\n", a + b);
	}
}