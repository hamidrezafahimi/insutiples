#include <pybind11/pybind11.h>

namespace py = pybind11;


class SomeClass 
{
  float multiplier;
public:
  SomeClass(float multiplier_) : multiplier(multiplier_) {};

  float multiply(float input) {
    return multiplier * input;
  }
};


PYBIND11_MODULE(module_name, module_handle) {

  py::class_<SomeClass>(
			module_handle, "PySomeClass"
			)
    .def(py::init<float>())
    .def("multiply", &SomeClass::multiply)
    ;
}