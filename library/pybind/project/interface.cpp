#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "header.h"

namespace py = pybind11;


PYBIND11_MODULE(module_name, module_handle) 
{
  py::class_<SomeClass>(
			module_handle, "PySomeClass"
			)
    .def(py::init<float>())
    .def(py::init<float, float>())
    .def("multiply_two", [](SomeClass &self, float one, float two) {
			   return py::make_tuple(self.multiply(one), self.multiply(two));
			 })
    ;
}