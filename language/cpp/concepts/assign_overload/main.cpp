#include <iostream>

struct Action
{
    virtual Action* operator+= (const Action*) = 0;
    // {
    //     Action *a;
    //     return a;
    // }
// private:
    int data = 1;
};

struct Selection: public Action
{
    Action* operator+= (const Action* p) override
    {
        data += p->data;
        return this;
    }
};

int main ()
{
    Action *aPtr1 = new Selection();
    Selection *aPtr2 = new Selection();
    
    static_cast<Selection*>(aPtr1)->operator+=(aPtr2);

    std::cout<<"data of aPtr1: "<<aPtr1->data<<"\n";

    return 0;
}