#include <iostream>
#include <vector>

template <typename T> 
inline void printLine(T& vec)
{
    for (auto &el: vec)
        std::cout<<el<<"\t";
    std::cout<<"\n";
}

template <typename T> 
void print2dArr(T& arr)
{
    for (auto &row: arr)
    {
        printLine(row);
    }
    std::cout<<"\n";
}

void print2d(std::vector<std::vector<int>> &inp)
{
    print2dArr(inp);
}


int main ()
{
    std::vector<std::vector<int>> arr;

    arr = std::vector<std::vector<int>> (2, std::vector<int> (4, 0));

    std::cout<<"before: \n";
    print2d(arr);

    arr.push_back(std::vector<int>(4, 0));

    std::cout<<"after: \n";
    print2d(arr);
}