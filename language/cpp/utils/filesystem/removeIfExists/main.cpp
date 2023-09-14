#include <filesystem>
#include <iostream>
#include <string>

int main()
{
  std::string searchfilename;
  std::cout << "Please enter the filename to be searched\n";
  std::cin >> searchfilename;
  try {
    if (std::filesystem::remove(searchfilename))
       std::cout << "file " << searchfilename << " deleted.\n";
    else
       std::cout << "file " << searchfilename << " not found.\n";
  }
  catch(const std::filesystem::filesystem_error& err) {
     std::cout << "filesystem error: " << err.what() << '\n';
  }
}