#include "iostream"
#include <random>
using namespace std;

// This program generates real random numbers which differ every instant the function is called, 
// no matter how close are the sequential call times.

size_t randomGenerator(size_t min, size_t max) {
    std::mt19937 rng;
    rng.seed(std::random_device()());
    std::uniform_int_distribution<std::mt19937::result_type> dist(min, max);
    return dist(rng);
}

int main()
{
    int a = 0, b = 100;
    cout << randomGenerator(a,b) << endl;
    return 0;
}