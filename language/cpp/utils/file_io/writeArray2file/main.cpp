
#include <vector>
#include <fstream>

int main()
{

std::vector<std::vector<int> > v {
    {1,2,3},
    {4,5,6},
    {7,8,9}
};

//do with v;
std::ofstream out("test.csv");

for (auto& row : v) {
  for (auto col : row)
    out << col <<',';
  out << '\n';
}
}