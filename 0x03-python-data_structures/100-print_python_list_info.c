#include <Python.h>
#include <object.h>
#include <listobject.h>
/*
 * print_python_list_info - functiionn tht prints the python info in c
 *@p: the pointer to the info
 *
 *Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int size_info = PyList_Size(p);
	int a;

	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size_info);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (a = 0; a < size_info; a++)
		printf("Element %i: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
}
