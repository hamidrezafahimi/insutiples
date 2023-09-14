#include <iostream>
#include <vector>

int main ()
{
    // using namespace std;

    std::vector <int> *v;

    v->push_back (50);
    v->push_back (1);
    v->push_back (987);
    v->push_back (1001);

    // Access objects in a vector using iterators:
    std::vector<int>::iterator i = v->begin();

    // i != v->end ();
    while (i != v->end ())
    {

    // std::cout << "El \n";
    size_t nElementIndex = std::distance (v->begin (),
                    i);

    std::cout << "Element at position ";
    std::cout << nElementIndex << " is: " << *i << std::endl;

    ++ i;
    // move to the next element
    }

    return 0;
}