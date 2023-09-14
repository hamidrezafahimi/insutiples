#include <iostream>
#include <vector>

struct Action_
{
    Action_(float _r, float _psi)
    {
        r = _r;
        psi = _psi;
    }

    float r;
    float psi;
};

union Action
{
    Action() {};
    ~Action() {};

    Action_ a;
    int l;
};

int main()
{
    Action act_1;
    Action act_2;

    act_1.a = Action_(2.3, 5.2);
    act_2.l = 1;

    std::cout<<"vec: "<<act_1.a.r<<"\t"<<act_1.a.psi<<"\n";
    std::cout<<"int: "<<act_2.l<<"\n";

    return 0;
}