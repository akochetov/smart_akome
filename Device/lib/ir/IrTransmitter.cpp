#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <wiringPi.h>

#include "IrTransmitter.h"


IrTransmitter::IrTransmitter()
{
    // reset input buffer data
    this->nPin = -1;
}

IrTransmitter::~IrTransmitter()
{
    //dtor
}

void IrTransmitter::setPin(int nPin)
{
    this->nPin = nPin;
    // prepare target pin to send data
    pinMode(this->nPin, OUTPUT);
    digitalWrite(this->nPin, LOW);
}

int IrTransmitter::getPin()
{
    return this->nPin;
}

void IrTransmitter::mark(unsigned int nLen)
{
    if (nLen==0) return;

    unsigned long now = micros();

    while ((micros()-now)<nLen)
    {
        digitalWrite(this->nPin,HIGH);
        delayMicroseconds(IR_HIGHTIME-IR_TIMING_OFFSET);
        digitalWrite(this->nPin,LOW);
        delayMicroseconds(IR_LOWTIME-IR_TIMING_OFFSET);
    }
}

void IrTransmitter::space(unsigned int nLen)
{
    if (nLen==0) return;

    //delayMicroseconds(nLen);
    unsigned long now = micros();

    while ((micros()-now)<nLen)
    {
        delayMicroseconds(10);
    }
}


void IrTransmitter::transmit(uint32_t code)
{
    this->transmitStart();

    for (unsigned char i=0;i<32;i++)
    {
        if (code & (1<<i))
            this->transmit1();
        else
            this->transmit0();
    }

    this->transmit1();
}

void IrTransmitter::transmitStart()
{
    this->mark(IR_START_HIGH_PULSE_LENGTH);
    this->space(IR_START_LOW_PULSE_LENGTH);
}

void IrTransmitter::transmit1()
{
    this->mark(IR_SHORT_HIGH_PULSE_LENGTH);
    this->space(IR_LONG_LOW_PULSE_LENGTH);
}

void IrTransmitter::transmit0()
{
    this->mark(IR_SHORT_HIGH_PULSE_LENGTH);
    this->space(IR_SHORT_LOW_PULSE_LENGTH);
}
