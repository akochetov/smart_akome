#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <wiringPi.h>

#include "IrReceiver.h"
#include "IrTransmitter.h"

#define RECEIVE_PIN 5
#define TRANSMIT_PIN 6

#define DATA 4278249232

int main()
{
    // sets up the wiringPi library
    if (wiringPiSetup () < 0)
    {
      fprintf (stderr, "Unable to setup wiringPi: %s\n", strerror (errno));
      return 0;
    }
    printf ("wiringPi has been successfully setup\r\n");

    IrReceiver irrx = IrReceiver();
    irrx.enableReceive(RECEIVE_PIN);

    IrTransmitter irtx = IrTransmitter();
    irtx.setPin(TRANSMIT_PIN);

    // display counter value every second.
    while ( 1 )
    {
        //irtx.transmit(DATA);
        //printf("Transmitted %u\r\n",DATA);

        if (irrx.available())
        {
            printf("Data received %u\r\n",irrx.getReceivedRawdata());
            irrx.resetAvailable();
        }

        delay( 500 );
    }

  return 0;
}
