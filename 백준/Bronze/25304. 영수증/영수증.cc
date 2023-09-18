#include <stdio.h>

int main(void) {
	int x; short n;
	scanf("%d\n%hd", &x, &n);
	int s = 0;
	for (short i = 0; i < n; i++) {
		int a; short b;
		scanf("%d%hd", &a, &b);
		s += a * b;
	}
	if (s == x) {
		printf("Yes");
	}
	else {
		printf("No");
	}
}