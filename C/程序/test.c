#include <stdio.h>
int main()
{
	int p;
	p = 23;
	printf("%d\n",p);
	printf("%d\n",*(&p));
	printf("%ld\n",&p);
	return 0;
}
