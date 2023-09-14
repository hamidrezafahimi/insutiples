#include <iostream>

using namespace std;

class Base{

public:

virtual void Output() = 0;

};

class Derived : public Base{

public:

void Output()

{
std::cout << "Class derived from the Base class." << std::endl;
}

};

int main(){

Base *bpointr;

Derived dpointr;

bpointr = &dpointr;

bpointr->Output();
return 0;

}