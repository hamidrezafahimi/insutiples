#include <iostream>

using namespace std;

class A
{
public:
    A (int a_)
    {
        a = a_;
    }

    virtual void transition() = 0;

private:
    int a;
};

class B: public A
{
public:
    B (int a_, int b_): A(a_)
    {
        b = b_;
    }

    void transition()
    {

    }

    virtual void solve()
    {}

private:
    int b;
};


class C: public B
{
public:
    C (int a_, int b_, int c_): B(a_, b_)
    {
        c = c_;
    }

    // void transition()
    // {

    // }


private:
    int c;
};

int main ()
{
    C cobj(1,2,3);
}