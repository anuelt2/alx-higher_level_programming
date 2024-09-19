#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: Pointer to a Python object
 *
 * Return: Void
 */

void print_python_list(PyObject *p)
{
	long int size;
	long int memory;
	long int index;
	PyObject **element;
	PyObject *item;

	size = PyList_Size(p);
	memory = ((PyListObject *)p)->allocated;
	element = ((PyListObject *)p)->ob_item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", memory);

	index = 0;
	while (index < size)
	{
		item = element[index];
		printf("Element %ld: %s\n", index, item->ob_type->tp_name);
		if (PyBytes_Check(item))
		{
			print_python_bytes(item);
		}
		index++;
	}
}

/**
 * print_python_bytes - Prints some basic info about Python bytes
 * @p: Pointer to a Python object
 *
 * Return: Void
 */

void print_python_bytes(PyObject *p)
{
	long int size;
	long int index;
	PyBytesObject *bytes;

	printf("[.] bytes object info\n");

	bytes = (PyBytesObject *)p;

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
	{
		size = 10;
	}
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}

	printf(" first %ld bytes: ", size);
	index = 0;
	while (index < size)
	{
		printf(" %02x", bytes->ob_sval[index]);
		if (index == size - 1)
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
		index++;
	}
}
