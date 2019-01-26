#include<stdio.h>

int main()
{
	int* pointer;
	int value = 5;
	
	pointer = &value;

	printf("value of pointer is %d\n", *pointer);

	return 0;
}
