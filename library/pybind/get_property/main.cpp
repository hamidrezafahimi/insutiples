#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

namespace py = pybind11;


class SomeClass 
{
  float multiplier;
public:
  SomeClass(float multiplier_) : multiplier(multiplier_) {};

  std::vector<std::vector<uint8_t>> make_image() 
  {
      auto out = std::vector<std::vector<uint8_t>>();
      for (auto i = 0; i < 128; i++) {
        out.push_back(std::vector<uint8_t>(64));
      }
      for (auto i = 0; i < 30; i++) {
        for (auto j = 0; j < 30; j++) { out[i][j] = 255; }
      }
      return out;
    }
};


PYBIND11_MODULE(module_name, module_handle) 
{
  py::class_<SomeClass>(
			module_handle, "PySomeClass"
			)
    .def(py::init<float>())
    .def_property_readonly("image", [](SomeClass &self) {
				      py::array out = py::cast(self.make_image());
				      return out;
				    })
    ;
}