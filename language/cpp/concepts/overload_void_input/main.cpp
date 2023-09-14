#include <iostream>
#include <string>

using namespace std;

template<>
double func<double, double>() {
    cout<<"one f\n";
    return 1.852;
}

template<typename d>
std::string func<int, std::string>() {
    cout<<"two f\n";
    return 1 / 1.852;
}


int main()
{


}