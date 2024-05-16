#include <iostream>
#include <vector>
#include <algorithm>

template <typename Tc>
int argMax(std::vector<Tc> inp)
{
    // std::vector<int>::iterator max = max_element(inp.begin(), inp.end());
    auto it = *max_element(inp.begin(), inp.end());
    // int ma
    std::vector<Tc> indices;
    for (Tc i = 0; i < inp.size(); i++)
    {
        if (inp[i] == it)
            indices.push_back(i);
    }
    std::cout<<indices.size()<<"\n";
    return it;
}

int main()
{
    std::vector<int> v{1,3,3,2,3,3};
    std::cout<<argMax(v)<<"\n";

    // std::vector<int>::iterator max = max_element(v.begin(), v.end());
    // int argmaxVal = distance(v.begin(), max); 
    // std::cout<<argmaxVal<<"\n";
}
