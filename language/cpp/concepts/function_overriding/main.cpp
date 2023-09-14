#include <iostream>

class A
{
public:
    virtual void a_func()
    {
        std::cout<<"in a\n";
    }
};

class B: public A
{
public:
    void a_func() override
    {
        std::cout<<"in b\n";
    }
};

class C: public A
{
public:
    void c_func()
    {
        std::cout<<"c func\n";
    }
};

int main()
{
    A *ab;
    A *ac;
    B b;
    C c;
    ab = &b;
    ac = &c;

    ab->a_func();
    ac->a_func();
    return 0;
}