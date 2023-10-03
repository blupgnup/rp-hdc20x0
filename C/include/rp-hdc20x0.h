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
// Note that this only affects the conversion speed
// LSBs are not controlled and should be masked when reading value
int set_temperature_resolution(int resolution);
    // 0 : High resolution
    // 1 : Medium resolution
    // 2 : Low resolution


// Set humidity resolution
// Note that this only affects the conversion speed
// LSBs are not controlled and should be masked when reading value
int set_humidity_resolution(int resolution);
    // 0 : High resolution
    // 1 : Medium resolution
    // 2 : Low resolution


#ifdef __cplusplus
}
#endif 

#endif
