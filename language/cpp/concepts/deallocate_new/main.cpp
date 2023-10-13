#include <iostream>

using namespace std;

class base {

public:

base (){

cout << "base constructor" << endl;

}

~base (){

cout << "base destructor" << endl;

}

};


int main()
{

base* bpointr = new base();

delete bpointr;

}
