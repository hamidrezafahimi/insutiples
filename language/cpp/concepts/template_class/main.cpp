// C++ Program to implement
// template Array class
#include <iostream>
using namespace std;

enum Multiplicity {SINGLE = 0, MULTIPLE = 1};

template <typename T> class All {
private:
    Multiplicity type;
 
protected:
    virtual T get() = 0;

public:
    All(Multiplicity m)
    {
        type = m;
    }
};

template <typename T> class Multiple: public All<T> {
public:
    Multiple(Multiplicity m): All<T>(m) {}
    T get() override {}
};


int main()
{
    Multiple<void> a(Multiplicity::MULTIPLE);
    return 0;
}