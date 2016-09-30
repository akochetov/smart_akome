#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <wiringPi.h>

#include "IrReceiver.h"

unsigned int IrReceiver::nReceivedBitlength = 0;
unsigned int IrReceiver::timings[IR_MAX_CHANGES];

IrReceiver::IrReceiver()
{
    // reset input buffer data
    this->nPin = -1;
}

IrReceiver::~IrReceiver()
{
    disableReceive();
}

void IrReceiver::setPin(int nPin)
{
    this->nPin = nPin;
}

int IrReceiver::getPin()
{
    return this->nPin;
}

void IrReceiver::enableReceive(int nPin)
{
    this->setPin(nPin);
    if (this->nPin == -1) return;

    // prepare target pin to receive data
    pinMode(this->nPin, INPUT);

    // reset input buffer data
    this->resetAvailable();

    // generate an interrupt on high-to-low transitions
    // and attach myInterrupt() to the interrupt
    if ( wiringPiISR (this->nPin, INT_EDGE_BOTH, &handleInterrupt) < 0 ) {
      fprintf (stderr, "Unable to setup ISR: %s\n", strerror (errno));
      return;
    }
    //printf ("Interrupt handler has been successfully setup for port %i\r\n",this->nPin);
}

void IrReceiver::disableReceive()
{
    setPin(-1);
}

bool IrReceiver::available()
{
    return IrReceiver::nReceivedBitlength != 0;
}

void IrReceiver::resetAvailable()
{
    IrReceiver::nReceivedBitlength = 0;
	for (unsigned char i=0;i<IR_MAX_CHANGES;i++)
		IrReceiver::timings[i] = 0;
}

unsigned int IrReceiver::getReceivedBitlength()
{
    return IrReceiver::nReceivedBitlength;
}

uint32_t IrReceiver::getReceivedRawdata()
{
	if (!IrReceiver::nReceivedBitlength) return 0;

    uint32_t result = 0;
    for (unsigned char i=IR_PROTOCOL_OFFSET;i<IrReceiver::nReceivedBitlength;i+=2)
    {
        //fix data errors
        if (IrReceiver::timings[i+1]*2 < IrReceiver::timings[i])
        {
            unsigned char temp = IrReceiver::timings[i+1];
            IrReceiver::timings[i+1] = IrReceiver::timings[i];
            IrReceiver::timings[i] = temp;
        }

        printf("%u, ",IrReceiver::timings[i]);
        printf("%u, ",IrReceiver::timings[i+1]);
        if (IrReceiver::timings[i+1] > 2*IrReceiver::timings[i])
            result+=pow(2,(i-IR_PROTOCOL_OFFSET)/2);
    }

	if (!result)
		this->resetAvailable();

    return result;
}

void IrReceiver::handleInterrupt()
{
    static unsigned int duration;
    static unsigned int changeCount;
    static unsigned long lastTime;

    long time = micros();
    duration = time - lastTime;

    if (duration < IR_NOISE_MIN_THRESHOLD || duration > IR_NOISE_MAX_THRESHOLD)
    {
        //printf("Filtereed out noise  %i\r\n",duration);
        lastTime = time;
        return;
    }

    // avoid samples to be less than 550
    if (duration < 550)
        duration = 550;
    // treat samples like 800 as short 500 samples
    if (duration > 550 && duration <1000)
        duration = 550;

    //printf("%i, ", duration);

    if ((duration > 5000 && IrReceiver::timings[0] > 5000) ||
        (IrReceiver::timings[0] > 5000 && changeCount >= IR_MAX_CHANGES))
{
	if (changeCount > 1)
    {
        //read data here
        IrReceiver::timings[changeCount++] = duration;
        IrReceiver::nReceivedBitlength = changeCount-1;

        changeCount = 0;
    }
}
    else if (duration > 5000)
    {
        // new message transmitting has started or is about to start
        changeCount = 0;
    }


    if (changeCount >= IR_MAX_CHANGES)
    {
        changeCount = 0;
    }

    IrReceiver::timings[changeCount++] = duration;
    lastTime = time;
}
