#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - d func gets data of d PyFloatObject
 * @p: d PyObject
 *
 * Return: Nothing
*/

void print_python_float(PyObject *p)
{
	double val;
	char *str = NULL;

	val = 0;
	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - d func gets data of d PyBytesObject
 * @p: d PyObject
 *
 * Return: Nothing
*/

void print_python_bytes(PyObject *p)
{
	Py_ssize_t sz, x;
	char *str = NULL;

	sz = 0:
	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sz = PyBytes_Size(p);
	printf("  size: %zd\n", sz);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", sz < 10 ? sz + 1 : 10);
	x = 0;
	while (x < sz + 1 && x < 10)
	{
		printf(" %02hhx", str[x]);
		x++;
	}
	printf("\n");
}

/**
 * print_python_list - d func gets data of d PyListObject
 * @p: d PyObject
 *
 * Return: Nothing
*/

void print_python_list(PyObject *p)
{
	Py_ssize_t sz;
	PyObject *m;
	int x;

	sz = 0;
	x = 0;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		sz = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", sz);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (x < sz)
		{
			m = PyList_GET_ITEM(p, x);
			printf("Element %d: %s\n", x, m->ob_type->tp_name);
			if (PyBytes_Check(m))
				print_python_bytes(m);
			else if (PyFloat_Check(m))
				print_python_float(m);
			x++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
