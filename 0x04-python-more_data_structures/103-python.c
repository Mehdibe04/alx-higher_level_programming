#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prnts byts info
 *
 * @p: py Obj
 *
 * Return: Nothing
*/

void print_python_bytes(PyObject *p)
{
	char *str;
	long int sz, j, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	sz = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", sz);
	printf("  trying string: %s\n", str);

	if (sz >= 10)
		lim = 10;
	else
		lim = sz + 1;

	printf("  first %ld bytes:", lim);

	for (j = 0; j < lim; j++)
		if (str[j] >= 0)
			printf(" %02x", str[j]);
		else
			printf(" %02x", 256 + str[j]);

	printf("\n");
}

/**
 * print_python_list - Prnts lst info
 *
 * @p: py Obj
 *
 * Return: Nothing
*/

void print_python_list(PyObject *p)
{
	long int sz, j;
	PyListObject *lst;
	PyObject *o;

	sz = ((PyVarObject *)(p))->ob_size;
	lst = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (j = 0; j < sz; j++)
	{
		o = ((PyListObject *)p)->ob_item[j];
		printf("Element %ld: %s\n", j, ((o)->ob_type)->tp_name);
		if (PyBytes_Check(o))
			print_python_bytes(o);
	}
}
