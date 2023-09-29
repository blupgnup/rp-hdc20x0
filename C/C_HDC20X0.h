#ifndef C_HDC20X0_H
#define C_HDC20X0_H

#include <stdint.h>    				//for uint





//negative on error, positive on success
int setup_hdc20x0();
int read_from_hdc20x0(float * temperature, float * humidity);





#endif
