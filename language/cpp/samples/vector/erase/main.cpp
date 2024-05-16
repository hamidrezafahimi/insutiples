

#include <iostream>
#include <vector>

int main ()
{
    std::vector<int> vec{1,2,3,4,5};
    int index = 2;
    vec.erase(vec.begin());

    for (auto& el: vec)
    {
        std::cout<<el<<"\t";
    }
    std::cout<<"\n";
}