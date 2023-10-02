#ifndef C_HDC20X0_H
#define C_HDC20X0_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>    				//for uint


// Setup sensor
// negative on error, positive on success
int setup_hdc20x0();

// Read temperature and humidity from sensor
// negative on error, positive on success
int read_from_hdc20x0(float * temperature, float * humidity);

// Turn on heater
int turn_heater_on();

// Turn off heater
int turn_heater_off();

// Set temperature resolution
int set_temperature_resolution(char resolution);

// Set humidity resolution
int set_temperature_resolution(char resolution);


#ifdef __cplusplus
}
#endif 

#endif
