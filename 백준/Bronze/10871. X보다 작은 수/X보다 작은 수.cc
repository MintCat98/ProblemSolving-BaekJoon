#include <stdio.h>

int main() {
	short n, x;
	scanf("%hd%hd", &n, &x);
	short* arr = new short[n];
	for (short i = 0; i < n; i++) {
		scanf("%hd", &arr[i]);
	}
	for (short i = 0; i < n; i++) {
		if (arr[i] < x) {
			printf("%hd ", arr[i]);
		}
	}
	delete[] arr;
}