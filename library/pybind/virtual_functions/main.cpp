#include <pybind11/pybind11.h>
#include <string>

class ExampleListener {
public:
    virtual ~ExampleListener() {}
    virtual void OnEvent(std::string const& s) = 0;
};

class PyExampleListener : public ExampleListener {
    using ExampleListener::ExampleListener;

    virtual void OnEvent(std::string const& s) {
        PYBIND11_OVERLOAD_PURE(void, ExampleListener, OnEvent, s);
    }
};

void call_listener(ExampleListener * listener) {
    listener->OnEvent("TestString");
}

namespace py = pybind11;

PYBIND11_PLUGIN(example) {
    py::module m("example", "pybind11 example plugin");

    py::class_<PyExampleListener>(m, "ExampleListener")
        .alias<ExampleListener>()
        .def(py::init<>())
        .def("OnEvent", &ExampleListener::OnEvent);

    m.def("call_listener", &call_listener);

    return m.ptr();
}