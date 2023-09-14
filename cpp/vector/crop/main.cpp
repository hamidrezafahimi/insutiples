#include <iostream>
#include <vector>

int main ()
{
    // using namespace std;

    std::vector <int> v;

    v.push_back (50);
    v.push_back (1);
    v.push_back (1001);
    v.push_back (987);
    v.push_back (1002);
    v.push_back (1003);
    v.push_back (1004);
    v.push_back (1005);

    // Access objects in a vector using iterators:
    std::vector <int> subV;
    subV = std::vector <int>(v.end()-5, v.end());

    for (auto & el : subV)
        std::cout<<el<<"\t";
    std::cout<<"\n";

    // i != v.end ();

    return 0;
}