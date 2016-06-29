/*
  Morse.h - Library for Livolo wireless switches.
  First version created by Sergey Chernov, October 25, 2013 for Arduino.
  Ported, adapted and simplified by M. Westenberg (Dec 2013).
  
  Released into the public domain.
*/

#ifndef Livolo_h
#define Livolo_h

#include <wiringPi.h>

//button code constants
#define BUTTON_A	8
#define BUTTON_B	16
#define BUTTON_C	56
#define BUTTON_D	42
#define BUTTON_1	0
#define BUTTON_2	96
#define BUTTON_3	120
#define BUTTON_4	24
#define BUTTON_5	80
#define BUTTON_6	48
#define BUTTON_7	108
#define BUTTON_8	12
#define BUTTON_9	72
#define BUTTON_10	40
#define BUTTON_OFF	106

class Livolo
{
  public:
    Livolo(unsigned char pin);
    void sendButton(unsigned int remoteID, unsigned char keycode);
  private:
    unsigned char txPin;
	int i; 						// just a counter
	unsigned char pulse; 		// counter for command repeat
	bool high; 					// pulse "sign"
	void selectPulse(unsigned char inBit);
	void sendPulse(unsigned char txPulse);
};

#endif