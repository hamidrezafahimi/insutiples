#include <iostream>
#include <string>

int main()
{
  std::string fn = "filename.conf";
  if(fn.substr(fn.find_last_of(".") + 1) == "conf") {
    std::cout << "Yes..." << std::endl;
  } else {
    std::cout << "No..." << std::endl;
  }
}