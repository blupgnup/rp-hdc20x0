#include "rp-hdc20x0.h"
#include <stdio.h>
#include <unistd.h>

int main()
{
	float temperature, humidity; 

	if(setup_hdc20x0() != 0 ) return 0; 
    
	for (int i = 0; i < 5; i++) {
		if(read_from_hdc20x0(&temperature, &humidity)!=0) return 0;

		printf("{ \"temperature\" : %.1f, \"humidity\" : %.1f }\n", temperature, humidity);
		sleep(1);
	}
    
    if(hdc20x0_heater_on() != 0 ) {
        printf("Unable to turn heater on");
        return -3;
    }
    
    printf("Turned heater on. Temperature should climb up:\n");
    for (int i = 0; i < 5; i++) {
		if(read_from_hdc20x0(&temperature, &humidity)!=0) return 0;

		printf("{ \"temperature\" : %.1f, \"humidity\" : %.1f }\n", temperature, humidity);
		sleep(1);
	}
    
    if(hdc20x0_heater_off() != 0 ) {
        printf("Unable to turn heater on");
        return -3;
    }    
    
    printf("Turned heater off. Temperature should drop off:\n");
    for (int i = 0; i < 5; i++) {
		if(read_from_hdc20x0(&temperature, &humidity)!=0) return 0;

		printf("{ \"temperature\" : %.1f, \"humidity\" : %.1f }\n", temperature, humidity);
		sleep(1);
	}

	return 0;
}
