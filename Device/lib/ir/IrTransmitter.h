#ifndef IRTRANSMITTER_H
#define IRTRANSMITTER_H

#include <stdint.h>


// Define carrier frequency related parameters
#define IR_DUTY_CYCLE 33// NEC protocol duty cycle 1/3
#define IR_CARRIER_FREQUENCY 38000 //38 KHz5;,aemt
#define IR_PERIOD 26//(1000000)/IR_CARRIER_FREQUENCY //1 sec / cf
#define IR_HIGHTIME 9//IR_PERIOD*IR_DUTY_CYCLE/100
#define IR_LOWTIME 15//IR_PERIOD-IR_HIGHTIME

// Timing offset in micros
#define IR_TIMING_OFFSET 0

// Start HIGH pulse length
#define IR_START_HIGH_PULSE_LENGTH 9000	//9000 original, 9048 according to lirc
#define IR_START_LOW_PULSE_LENGTH 4466  //4476 original or 4500, 4446 according to lirc
#define IR_SHORT_HIGH_PULSE_LENGTH 560  //564 original, or 560, 581 according to lirc
#define IR_SHORT_LOW_PULSE_LENGTH 536   //546 original, or 560, 539 according to lirc
#define IR_LONG_LOW_PULSE_LENGTH 1660	//1672 original, or 1690, 1657 according to lirc

class IrTransmitter
{
    public:
        IrTransmitter();
        virtual ~IrTransmitter();

        void setPin(int nPin);
        int getPin();

        void transmit(uint32_t code);
    protected:
    private:
        int nPin;

        void transmitStart();
        void transmit0();
        void transmit1();
        void mark(unsigned int nLen);
        void space(unsigned int nLen);
};

#endif // IRTRANSMITTER_H
