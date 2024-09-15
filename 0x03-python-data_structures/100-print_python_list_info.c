#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Prints some basic info baout Python lists
 * @p: Pointer to a Python list object
 *
 * Return: Void
 */

void print_python_list_info(PyObject *p)
{
	long int size;
	long int memory;
	long int index;
	PyObject *element;

	size = PyList_Size(p);
	memory = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", memory);

	index = 0;
	while (index < size)
	{
		element = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, Py_TYPE(element)->tp_name);
		index++;
	}
}
