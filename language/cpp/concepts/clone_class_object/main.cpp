#include <iostream>
using namespace std;

class Foo
{ 
public:
    int num = 1;

    Foo() {};
    Foo& operator=(const Foo& rhs) {};
};



int main()
{
    Foo orig;
    Foo copy = orig;  // clones orig if implemented correctly

    copy.num++;

    std::cout<<orig.num<<"\n";
    std::cout<<copy.num<<"\n";
}