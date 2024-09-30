#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints some basic info about Python lists objects
 * @p: PyListObject
 *
 * Return: Void
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t memory;
	Py_ssize_t idx;
	const char *type;

	size = ((PyVarObject *)p)->ob_size;
	memory = ((PyListObject *)p)->allocated;
	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", memory);
	idx = 0;
	while (idx < size)
	{
		type = ((PyListObject *)p)->ob_item[idx]->ob_type->tp_name;
		printf("Element %ld: %s\n", idx, type);
		if (strcmp(type, "bytes") == 0)
		{
			print_python_bytes(((PyListObject *)p)->ob_item[idx]);
		}
		else if (strcmp(type, "float") == 0)
		{
			print_python_float(((PyListObject *)p)->ob_item[idx]);
		}
		idx++;
	}
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: PyBytesObject
 *
 * Return: Void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t idx;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
	{
		size = 10;
	}
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %ld bytes: ", size);
	idx = 0;
	for (idx = 0; idx < size; idx++)
	{
		printf("%02hhx", ((PyBytesObject *)p)->ob_sval[idx]);
		if (idx == (size - 1))
		{
			printf("\n");
		}
		else
		{
			printf(" ");
		}
		idx++;
	}
}

/**
 * print_python_float - Prints some basic info about Python float objects
 * @p: PyFloatObject
 *
 * Return: Void
 */

void print_python_float(PyObject *p)
{
	char *buf;

	buf = NULL;
	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buf = PyOS_double_to_string(((PyFloatObject *)p)->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
}
