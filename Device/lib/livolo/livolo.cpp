#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <netdb.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include "livolo.h"

#define REPEATS 50

// Global Variables
//
unsigned int group = 23783;							// The 23783 is the group value of my little switch (bit 0-15)
unsigned char device = 8;							// Key A is number 8, B16 (bit 16-22, with bit 19=1)
unsigned int loops = 1;
unsigned int repeats = REPEATS;
bool inverted = false;

unsigned char fflg = 0;										// Fake flag, for debugging. Init to false. If true, print values only

// I found the timing parameters below to be VERY VERY critical
// Only a few uSecs extra will make the switch fail.
// https://wiki.pilight.org/livolo_switch_v7_0
unsigned int p_short = 170;									// Originally 160. With WiringPi hi prio 150 seems to work best
unsigned int p_long = 340;									// Originally 320. With WiringPi hi prio 305 seems to work best
unsigned int p_start = 595;									// Originally 520. With WiringPi hi prio 520 seems to work best

Livolo::Livolo(unsigned char pin)
{
  pinMode(pin, OUTPUT);
  txPin = pin;
}

// keycodes #1: 0, #2: 96, #3: 120, #4: 24, #5: 80, #6: 48, #7: 108, #8: 12, #9: 72; #10: 40, #OFF: 106
// real remote IDs: 6400; 19303; 23783
// tested "virtual" remote IDs: 10550; 8500; 7400
// other IDs could work too, as long as they do not exceed 16 bit
// known issue: not all 16 bit remote ID are valid
// have not tested other buttons, but as there is dimmer control, some keycodes could be strictly system
// use: sendButton(remoteID, keycode), see example blink.ino; 

// =======================================================================================
//
//
void Livolo::sendButton(unsigned int remoteID, unsigned char keycode) {
  // start transmitting base frequency if not inverted
  //if (!inverted) {
  //    digitalWrite(txPin, HIGH);
  //    delayMicroseconds(p_start); 
  //}

  for (pulse= 0; pulse <= repeats; pulse++) 		// how many times to transmit a command
  {
        // start transmitting base frequency if not inverted
        if (!inverted) {
          digitalWrite(txPin, HIGH);
          //delayMicroseconds(p_start * 2);
        }

  	high = !inverted;								// if inverted, start invert all pulses
	if (high) 
		sendPulse(1);
    else 
		sendPulse(0);								// Start 
    												// first pulse is always high

    for (i = 15; i>=0; i--) { 						// transmit remoteID
      unsigned int txPulse = remoteID & ( 1<<i );	// read bits from remote ID
      if (txPulse>0) { 
		selectPulse(1); 
      }
      else {
		selectPulse(0);
      }
    }

    for (i = 6; i>=0; i--) 							// XXX transmit keycode
    {
		unsigned char txPulse= keycode & (1<<i); 	// read bits from keycode
		if (txPulse>0) {
			selectPulse(1); 
		}
		else {
			selectPulse(0);
		}
    } 
    if (fflg==1) printf("\n");
  }
  
  // always put to LOW to avoid transmitter constantly generating radio wave when idle
  digitalWrite(txPin, LOW);
}

// =======================================================================================
// build transmit sequence so that every high pulse is followed by low and vice versa
//
//
void Livolo::selectPulse(unsigned char inBit) {

    switch (inBit) {
    	case 0: 
        if (high == true) {   						// if current pulse should be high, send High Zero
		sendPulse(2); 
		sendPulse(4);
        } else {              						// else send Low Zero
 		sendPulse(4);
		sendPulse(2);
        }
	break;

	case 1:                						// if current pulse should be high, send High One
        if (high == true) {
		sendPulse(3);
        } else {             						// else send Low One
		sendPulse(5);
        }
        high=!high; 								// invert next pulse
	break; 
    }

}

// =========================================================================================
// transmit pulses
// slightly corrected pulse length, use old (commented out) values if these not working for you

void Livolo::sendPulse(unsigned char txPulse) {
  if (fflg == 0)
  {
	switch(txPulse) 								// transmit pulse
	{
	case 0: 										// Start
		digitalWrite(txPin, LOW);
		delayMicroseconds(p_start); 				// 550
	break;
   
	case 1: 										// Start
		digitalWrite(txPin, HIGH);
		delayMicroseconds(p_start); 				// 550
	break;

	case 2: 										// "High Zero"
		digitalWrite(txPin, LOW);
		delayMicroseconds(p_short); 				// 110
	break;
 
	case 3: 										// "High One"
		digitalWrite(txPin, LOW);
		delayMicroseconds(p_long); 					// 303
	break; 

	case 4: 										// "Low Zero"
		digitalWrite(txPin, HIGH);
		delayMicroseconds(p_short);					// 110
	break;

	case 5:											// "Low One"
		digitalWrite(txPin, HIGH);
		delayMicroseconds(p_long); 					// 293
	break; 
	}
  }
  //
  // Fake, print only values, do not write to GPIO
  // This is very useful for debugging codes
  //
  else			 										
  {
  	switch(txPulse) {
		case 0:
			printf("L%d ",p_start);
		break;
		
		case 1:
			printf("H%d ",p_start);
		break;
		
		case 2:
			printf("L%d ",p_short);
		break;
		
		case 3:
			printf("L%d ",p_long);
		break;
		
		case 4:
			printf("H%d ",p_short);
		break;
		
		case 5:
			printf("H%d ",p_long);
		break;
	}
  }
}
