
from distutils.core import setup, Extension

setup(name             = 'IRRxTx',
      version          = '1.0',
      description      = 'Send and receive IR signals, NEC protocol, 38 KHzA module to control livolo light switches over 433 MHz radio channel',
      keywords         = 'IR Infrared',
      url              = '',
      ext_modules      = [Extension('IRRxTx',sources=['IrReceiver.cpp', 'IrTransmitter.cpp', 'python_wrap.cpp'],libraries=['wiringPi'],extra_compile_args=['-Wno-write-strings'])])
