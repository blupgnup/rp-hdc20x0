# rp-hdc20x0

Read Ti's HDC20X0 family sensors from a RedPitaya board

Adapted from SDL_Pi_HDC1000 and Pi_HDC2080 library

## Installation and use as an external library

Navigate to the C folder and run make and make install to install the library
Library is install by default in /opt/redpitaya. Please adapt LIB_DIR and LIB_DIR and INCLUDE_DIR to the wanted path if needed.

## Using the library

Just include the library in your application:
*#include "rp-hdc20x0.h"*

Do not forget to include appropriate folder when compiling...
