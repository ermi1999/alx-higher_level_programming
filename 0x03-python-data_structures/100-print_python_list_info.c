#include <Python.h>
/*
 * print_python_list_info - Prints information about a Python list
 * @p: Pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = PyList_Size(p);
	Py_ssize_t allocated_s = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", list_size);
	printf("[*] Allocated = %zd\n", allocated_s);
	Py_ssize_t i;

	for (i = 0; i < list_size; i++)
	{
		const char *element_name;

		PyObject *element = PyList_GetItem(p, i);
		PyObject *element_type = PyObject_Type(element);

		element_name = ((PyTypeObject *)element_type)->tp_name;
		printf("Element %ld: %s\n", i, element_name);
		Py_DECREF(element_type);
	}
}

