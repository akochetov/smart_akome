#include <python.h>
#include "livolo.h"


void define_constants(PyObject *module)
{
	btn_a = Py_BuildValue("b",  BUTTON_A);PyModule_AddObject(module, "BUTTON_A", btn_a);
	btn_b = Py_BuildValue("b",  BUTTON_B);PyModule_AddObject(module, "BUTTON_B", btn_b);
	btn_c = Py_BuildValue("b",  BUTTON_C);PyModule_AddObject(module, "BUTTON_C", btn_c);
	btn_d = Py_BuildValue("b", BUTTON_D);PyModule_AddObject(module, "BUTTON_D", btn_d);
	btn_1 = Py_BuildValue("b", BUTTON_1);PyModule_AddObject(module, "BUTTON_1", btn_1);
	btn_2 = Py_BuildValue("b", BUTTON_2);PyModule_AddObject(module, "BUTTON_2", btn_2);
	btn_3 = Py_BuildValue("b", BUTTON_3);PyModule_AddObject(module, "BUTTON_3", btn_3);
	btn_4 = Py_BuildValue("b", BUTTON_4);PyModule_AddObject(module, "BUTTON_4", btn_4);
	btn_5 = Py_BuildValue("b", BUTTON_5);PyModule_AddObject(module, "BUTTON_5", btn_5);
	btn_6 = Py_BuildValue("b", BUTTON_6);PyModule_AddObject(module, "BUTTON_6", btn_6);
	btn_7 = Py_BuildValue("b", BUTTON_7);PyModule_AddObject(module, "BUTTON_7", btn_7);
	btn_8 = Py_BuildValue("b", BUTTON_8);PyModule_AddObject(module, "BUTTON_8", btn_8);
	btn_9 = Py_BuildValue("b", BUTTON_9);PyModule_AddObject(module, "BUTTON_9", btn_9);
	btn_10 = Py_BuildValue("b", BUTTON_10);PyModule_AddObject(module, "BUTTON_10", btn_10);
	btn_OFF = Py_BuildValue("b", BUTTON_OFF);PyModule_AddObject(module, "BUTTON_OFF", btn_OFF);
}

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
	{"sendButton", py_sendButton, METH_VARARGS, "Send button code to Livolo switch\npin - wiringPi pi number (may differ from GPIO pin number)\nremoteID - ID of a physical or virtual remote, usually X*3 value where X is any integer, but other values may also work. Working codes: 6400, 26088, 23783.\ncode - button code (use BUTTON_* constants or put alternative values)."},
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
