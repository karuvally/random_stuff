#include<stdio.h>


// the main function
int main()
{
	// essential variables
	char buffer[255];

	// open the file
	FILE *bat_file;
	bat_file = fopen("/sys/class/power_supply/BAT0/capacity", "r");

	// try to read contents
	fgets(buffer, 255, bat_file);

	// print the contents
	printf("%s", buffer);

	// happily exit
	return 0;
}
