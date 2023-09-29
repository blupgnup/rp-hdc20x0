#include "rp-hdc20x0.h"
#include <stdio.h>
#include <unistd.h>

int main()
{
	float temperature, humidity; 

	if(setup_hdc20x0() != 0 ) return 0; 

	for (int i = 0; i < 10; i++) {
		if(read_from_hdc20x0(&temperature, &humidity)!=0) return 0;

		printf("{ \"temperature\" : %.1f, \"humidity\" : %.1f }\n", temperature, humidity);
		sleep(2);
	}

	return 0;
}
