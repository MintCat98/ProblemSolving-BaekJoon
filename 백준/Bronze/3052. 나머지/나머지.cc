#include <stdio.h>
#include <set>

int main() {
	std::set<int> s;
	short n;
	for (short i = 0; i < 10; i++) {
		scanf("%hd", &n);
		s.insert(n % 42);
	}
	printf("%d", s.size());
	return 0;
}