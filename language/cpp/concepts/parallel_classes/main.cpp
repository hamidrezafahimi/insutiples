#include <iostream>

//  What I wanted:  D -> C -> B -> A <- Y,Z
// But I didn't make it!
// Final topology:
// D -> C -> B (It seems that making B -> A does not help! because an auto pointer to Y or Z os passed
// to D...B branch and in B, an A class that is inherited does not help at all) 
// Y,Z -> A


class A
{
public:
    A () {}

    A (int a_)
    {
        a = a_;
    }

    virtual void bodyInDerived() {};
    // {

    virtual void transition()=0;
    // }
    void similarFunc()
    {
        std::cout<<"call to similar in a\n";
    }

protected:
    void trans()
    {
        std::cout<<"call to trans in a\n";
    }

private:
    int a;
};


class Z: public A
{
public:
    Z (int a_, int z_): A(a_)
    {
        z = z_;
    }

    void bodyInDerived()
    {
        std::cout<<"call to body in z in z\n";
    }

    void transition()
    {
    }

private:
    int z;
};


class Y: public A
{
public:
    Y (int a_, int z_): A(a_)
    {
        z = z_;
    }

    void bodyInDerived()
    {
        std::cout<<"call to body in z in y\n";
    }

    void similarFunc()
    {
        std::cout<<"call to similar in y\n";
    }


private:
    void transition()
    {
        std::cout<<"call to transition in y\n";
    }
    int z;
};


// class B: public A
class B 
{
public:
    // B () {}

    // B (int a_, int b_): A(a_)
    // {
    //     b = b_;
    // }

    B (auto* zPtr, int a_, int b_): A(a_)
    {
        b = b_;
        env = zPtr;
        // this = zPtr;
    }

    // B (Y* yPtr, int a_, int b_): A(a_)
    // {
    //     b = b_;
    //     env = yPtr;
    //     // this = zPtr;
    // }

    void transition()
    {
        env->similarFunc();
        similarFunc();
        trans();
        env->transition();
    }

    virtual void solve()
    {}

private:
    int b;
    A *env;
};


class C: public B
{
public:
    C (auto* zPtr, int a_, int b_, int c_): B(zPtr, a_, b_)
    // C (int a_, int b_, int c_): B(a_, b_)
    {
        c = c_;
    }

    // C ()
    // {}

    void test()
    {
        // this->bodyInDerived();
    }

private:
    int c;
};


class D: public C
{
public:
    D (auto* zPtr, int a_, int b_, int c_, int d_): C(zPtr, a_, b_, c_)
    // D (int a_, int b_, int c_, int d_): C(a_, b_, c_)
    {
        d = d_;
    }

    // D()
    // {
    // }

    void bodyInDerived() {}

private:
    int d;
};


int main ()
{
    Y obj(7, 8);
    // Z obj(7, 8);
    D dobj(&obj, 1, 2, 3, 4);
    
    // D dobj(1, 2, 3, 4);

    // D* dobj(new D());
    // D *dobj;
    
    // dobj = new D();
    
    // D *dobj;
    // dobj = &obj;
    
    dobj.transition();
}