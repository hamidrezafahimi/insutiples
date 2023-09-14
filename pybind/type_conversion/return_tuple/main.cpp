#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;


class SomeClass 
{
  float multiplier;
public:
  SomeClass(float multiplier_) : multiplier(multiplier_) {};

  float multiply(float input)
  {
    return multiplier * input;
  }

  py::tuple multiply_two(float one, float two) 
  {
    return py::make_tuple(multiply(one), multiply(two));
  }

};


PYBIND11_MODULE(module_name, module_handle) 
{
  py::class_<SomeClass>(
			module_handle, "PySomeClass"
			)
    .def(py::init<float>())
    .def("multiply_two", &SomeClass::multiply_two)
    ;
}