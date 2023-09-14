#include <iostream>

using namespace std;

class base {

public:

virtual void show(){

cout << "show base class" << endl;

}

void print(){

cout << "print base class" << endl;

}

};

class derived : public base {

public:

private:
void show(){

cout << "show derived class" << endl;

}

void print(){

cout << "print derived class" << endl;

}

};

int main()
{

base* bpointr;

derived dev;

bpointr = &dev;

// runtime binding

bpointr->show();

// compile time binding

bpointr->print();

}