#include <iostream>

class A
{
public:
    A(int a_)
    {
        a = a_;
    }

    void play()
    {
        std::cout<<"call to play function from base class\n";
        transition();
        // this->transition();
    }

protected:

private:

    virtual void transition() = 0;
    int a;
};

class B: public A
{
public:
    B(int a_, int b_): A(a_)
    {
        b = b_;
    }

private:
    void transition()
    {
        std::cout<<"call to transition function from B\n";
    }
    
    int b;
};

class C: public A
{
public:
    C(int a_, int b_): A(a_)
    {
        b = b_;
    }

private:
    void transition()
    {
        std::cout<<"call to transition function from C\n";
    }
    
    int b;
};

int main()
{
    B bObj(2,1);
    bObj.play();
    return 0;
}