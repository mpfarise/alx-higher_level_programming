#include <python.h>

/**
 * print_python_list_info - print basic info about python lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((Pylist*)p)->allocated;

	printf("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_Get_Item(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
