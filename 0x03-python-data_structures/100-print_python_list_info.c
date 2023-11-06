#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int sz = PyList_Size(p);
	int x = 0;
	PyListObject *j = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = %li\n", j->allocated);
	for (; x < sz; x++)
		printf("Element %i: %s\n", x, Py_TYPE(j->ob_item[x])->tp_name);
}
