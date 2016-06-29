#include <python.h>
#include "livolo.h"

// python function value = sendButton(pin, remoteID, code)
static PyObject *sendButton(PyObject *self, PyObject *args)
{
	unsigned char pin = 0;
	unsigned int remoteID = 0;
	unsigned char code = 0;
	PyObject *value;

	if (!PyArg_ParseTuple(args, "bIb", &pin, &remoteID, &code))
		return NULL;

	// check remoteID was specified
	if (remoteID == 0)
	{
		PyErr_SetString(PyExc_RuntimeError, "RemoteID can not be 0 or None.");
		return NULL;
	}

	Livolo liv(pin);
  
	if (wiringPiSetup () == -1)
	{
		PyErr_SetString(PyExc_RuntimeError, "WiringPI is not properly setup.");
		return NULL;
	}

	liv.sendButton(remoteID, code);

	return 1;
}


static const char moduledocstring[] = "Controlling Livolo light switches with 433 Mhz";

PyMethodDef livolo_methods[] = {
	{"sendButton", py_sendButton, METH_VARARGS, "Send button code to Livolo switch\npin - wiringPi pi number (may differ from GPIO pin number)\nremoteID - ID of a physical or virtual remote, usually X*3 value where X is any integer, but other values may also work. Working codes: 6400, 26088, 23783.\ncode - button code. Key #A: 8, #B: 16, #C: 56, #D: 42. For numeric buttons: #1: 0, #2: 96, #3: 120, #4: 24, #5: 80, #6: 48, #7: 108, #8: 12, #9: 72; #10: 40, #OFF: 106"},
   {NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION > 2
static struct PyModuleDef livolomodule = {
   PyModuleDef_HEAD_INIT,
   "livolo",      // name of module
   moduledocstring,  // module documentation, may be NULL
   -1,               // size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
   livolo_methods
};
#endif

#if PY_MAJOR_VERSION > 2
PyMODINIT_FUNC PyInit__livolo(void)
#else
PyMODINIT_FUNC init_livolo(void)
#endif
{
   int i;
   PyObject *module = NULL;

#if PY_MAJOR_VERSION > 2
   if ((module = PyModule_Create(&livolomodule)) == NULL)
      return NULL;
#else
   if ((module = Py_InitModule3("livolo", livolo_methods, moduledocstring)) == NULL)
      return;
#endif

   define_constants(module);

#if PY_MAJOR_VERSION > 2
   return module;
#else
   return;
#endif
}
