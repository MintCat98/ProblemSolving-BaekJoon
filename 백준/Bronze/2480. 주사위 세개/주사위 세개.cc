#include <stdio.h>
#include <set>
int main(void) {
	short a, b, c, l;
	std::set<short> s;
	scanf("%hd %hd %hd", &a, &b, &c);
	s.insert(a); s.insert(b); s.insert(c);
	l = s.size();
	if (l == 1) {
		printf("%hd", 10000 + a * 1000);
	}
	else if (l == 2) {
		short d;
		if (a == b) {
			d = a;
		}
		else if (a == c) {
			d = a;
		}
		else {
			d = b;
		}
		printf("%hd", 1000 + d * 100);
	}
	else {
		printf("%hd", *s.rbegin() * 100);
	}
}