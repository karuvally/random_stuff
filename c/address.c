#include<stdio.h>

int main()
{
	int var = 7;
	printf("The variable has value %d and address %u\n", var, &var);
	printf("This is fun -> %d\n", *&var);
	return 0;
}
