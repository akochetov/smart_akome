#include <Python.h>
#include <wiringPi.h>
#include <map>
#include "IrReceiver.h"
#include "IrTransmitter.h"

static std::map <int,IrReceiver*> receivers;

// python function to setup wiringPi with wiringPi numbering
static PyObject *py_setup(PyObject *self, PyObject *args)
{
	if (wiringPiSetup () == -1)
	{
		PyErr_SetString(PyExc_RuntimeError, "WiringPI is not properly setup.");
		return NULL;
	}

Py_RETURN_NONE;
}

// python function to setup wiringPi with GPIO numbering
static PyObject *py_setupGPIO(PyObject *self, PyObject *args)
{
	if (wiringPiSetupGpio () == -1)
	{
		PyErr_SetString(PyExc_RuntimeError, "WiringPI is not properly setup.");
		return NULL;
	}

	Py_RETURN_NONE;
}

// python function irTransmit(pin, code)
static PyObject *py_irTransmit(PyObject *self, PyObject *args)
{
	unsigned char pin = 0;
	unsigned int code = 0;

	if (!PyArg_ParseTuple(args, "bI", &pin, &code))
		return NULL;

	piHiPri(99);
    IrTransmitter irtx = IrTransmitter();
    irtx.setPin(pin);
	irtx.transmit(code);
	piHiPri(0);

	Py_RETURN_NONE;
}

static PyObject *py_irEnableReceive(PyObject *self, PyObject *args)
{
	unsigned char pin = 0;

	if (!PyArg_ParseTuple(args, "b", &pin))
		return NULL;

    //erase receiver at this position if exists
    IrReceiver* irrx = receivers[pin];
    receivers.erase(pin);
    delete irrx;

    receivers[pin] = new IrReceiver();
    receivers[pin]->enableReceive(pin);

	piHiPri(99);

    Py_RETURN_NONE;
}


static PyObject *py_irDisableReceive(PyObject *self, PyObject *args)
{
	unsigned char pin = 0;

	if (!PyArg_ParseTuple(args, "b", &pin))
		return NULL;

    IrReceiver* irrx = receivers[pin];
    receivers.erase(pin);
    delete irrx;

	piHiPri(0);

    Py_RETURN_NONE;
}

// python function irReceive(pin)
static PyObject *py_irReceive(PyObject *self, PyObject *args)
{
	unsigned char pin = 0;
	unsigned int result = 0;

	if (!PyArg_ParseTuple(args, "b", &pin))
		return NULL;

    IrReceiver* irrx = receivers[pin];

    if (!irrx)
    {
        PyErr_SetString(PyExc_RuntimeError, "IR receiver was not setup. Forgot to call irEnableReceive?");
        return NULL;
    }

    if (irrx->available())
    {
        result = irrx->getReceivedRawdata();
        if (result) irrx->resetAvailable();
    }

	return Py_BuildValue("I",result);
}

static const char moduledocstring[] = "Send and receive IR signals, NEC protocol, 38 KHz";

PyMethodDef ir_methods[] = {
	{"irTransmit", py_irTransmit, METH_VARARGS, "Send code via IR. pin is for IR LED, and code is a unsigned int code to send."},
	{"irReceive", py_irReceive, METH_VARARGS, "Blocking function to receive data from IR. pin is for IR LED. To cancel call irStopReceive. Returns 0 if no data received."},
	{"irEnableReceive", py_irEnableReceive, METH_VARARGS, "Creates IR receiver for specified port and starts receiving data."},
	{"irDisableReceive", py_irDisableReceive, METH_VARARGS, "Stops and deletes IR receiver for specified port."},
	{"setup", py_setup, METH_VARARGS, "Must be called before any other  method to initiate wiringPi. Uses wiringPi pins table."},
	{"setupGPIO", py_setupGPIO, METH_VARARGS, "Must be called before any other  method to initiate wiringPi. Uses GPIO pins table."},
	{NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION > 2
static struct PyModuleDef ir_module = {
   PyModuleDef_HEAD_INIT,
   "IRRxTx",      // name of module
   moduledocstring,  // module documentation, may be NULL
   -1,               // size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
   ir_methods
};
#endif

#if PY_MAJOR_VERSION > 2
PyMODINIT_FUNC PyInitIRRxTx(void)
#else
PyMODINIT_FUNC initIRRxTx(void)
#endif
{
   PyObject *module = NULL;

#if PY_MAJOR_VERSION > 2
   if ((module = PyModule_Create(&ir_module)) == NULL)
      return NULL;
#else
   if ((module = Py_InitModule3("IRRxTx", ir_methods, moduledocstring)) == NULL)
      return;
#endif

//   define_constants(module);

#if PY_MAJOR_VERSION > 2
   return module;
#else
   return;
#endif
}
