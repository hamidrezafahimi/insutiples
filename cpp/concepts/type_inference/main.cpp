#include <iostream>
#include <vector>

using namespace std;

union X
{
    int i;
    float f;
};

union Y
{
    int i;
    float f;
};

struct State
{
    State(int in1, int in2)
    {
        x.i = in1;
        y.i = in2;
    }

    State(float in1, float in2)
    {
        x.f = in1;
        y.f = in2;
    }

    // float getX() { return x.f };
    // float getY() { return y.f };
    // int getX() { return x.i };
    // int getY() { return x.i };

    X x;
    Y y;
    int *index;
};


int main()
{

State s(1,2);
State s2(float(1.2),float(2.2));

// float s2x = s2.getX();

std::vector<int> vec{1,2,3};

s2.index = &vec[0];

std::cout<<s2.index<<endl;
std::cout<<*s2.index<<endl;

return 0;
}