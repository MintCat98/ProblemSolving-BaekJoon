#include <stdio.h>
int main(void) {
	int a, b;
	scanf("%d\n%d", &a, &b);
	int b3 = b / 100;
	int b2 = (b - b3*100) / 10;
	int b1 = b - b3*100 - b2*10;
	printf("%d\n%d\n%d\n%d", a * b1, a * b2, a * b3, a * b);
}