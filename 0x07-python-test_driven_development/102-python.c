#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - The func prints info abt Py strs
 *
 * @p: A PyObj str obj
 *
 * Return: Nothing
*/

void print_python_string(PyObject *p)
{

	PyObject *s, *pr;

	(void)pr;
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	pr = PyObject_Repr(p);
	s = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(s));
}
