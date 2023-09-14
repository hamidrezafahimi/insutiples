#include <iostream>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <vector>


template<typename Iter_T>
float vectorNorm(Iter_T vec) {
  return std::sqrt(std::inner_product(vec.begin(), vec.end(), vec.begin(), 0.0L));
}

int main() {
//   int v[] = { 3, 4 };
  std::vector v = { 3, 4 };
  std::cout << "The length of the vector (3,4) is ";
  std::cout << vectorNorm(v) << std::endl;
}