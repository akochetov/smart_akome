
from distutils.core import setup, Extension

setup(name             = 'livolo',
      version          = '1.0',
      description      = 'A module to control livolo light switches over 433 MHz radio channel',
      keywords         = 'livolo 433 MHz',
      url              = '',
      ext_modules      = [Extension('livolo',['livolo.cpp', 'livolo.h', 'python_wrap.c'])])
