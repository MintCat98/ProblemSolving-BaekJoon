#include <stdio.h>

int count(int* arr, int size, int n);

int main() {
	int n;
	scanf("%d", &n);
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	int t;
	scanf("%d", &t);
	printf("%d", count(arr, n, t));
	delete[] arr;
	return 0;
}

int count(int* arr, int size, int n) {
	int c = 0;
	for (int i = 0; i < size; i++) {
		if (arr[i] == n) {
			c++;
		}
	}
	return c;
}