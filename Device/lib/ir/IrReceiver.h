#ifndef IRRECEIVER_H
#define IRRECEIVER_H

#include <stdint.h>

// Number of maximum High/Low changes per packet.
// We can handle up to (unsigned long) => 32 bit * 2 H/L changes per bit + 2 for sync
#define IR_MAX_CHANGES 66

// Minimum possible low-to-high transition speed to filter out noise. Microseconds
#define IR_NOISE_MIN_THRESHOLD 100
#define IR_NOISE_MAX_THRESHOLD 10000

// NIC IR protocol bits offset - 2 starting bits dont carry any data, so start read from bit 2 (starting bit position is 0)
#define IR_PROTOCOL_OFFSET 2

class IrReceiver
{
    public:
        IrReceiver();
        virtual ~IrReceiver();

        void setPin(int nPin);
        int getPin();

        void enableReceive(int nPin);
        void disableReceive();

        bool available();
        void resetAvailable();

        unsigned int getReceivedBitlength();
        uint32_t getReceivedRawdata();
    protected:
    private:
        int nPin;

        static unsigned int nReceivedBitlength;
        static unsigned int timings[IR_MAX_CHANGES];

        static void handleInterrupt();
};

#endif // IRRECEIVER_H
