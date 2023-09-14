#include <iostream>
#include <cmath>

int main ()
{
    int i = 3;
    float j = 10;
    float a = 2.37;
    std::cout<<std::round(a)<<"\n";
    std::cout<<std::round(a+0.5)<<"\n";
    std::cout<<i/j<<"\n";
    std::cout<<j/i<<"\n";
    int m = 2;
    float n = 2;
    bool b = m==n;
    std::cout<<b<<"\n";
}