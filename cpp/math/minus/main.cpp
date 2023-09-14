#include <iostream>
#include <algorithm>

int main()
{
    // Both works:

    // int first[] = { 100, 200, 300, 400, 500 };
    // int second[] = { 10, 20, 30, 40, 50 };

    std::vector<int> first = { 100, 200, 300, 400, 500 };
    std::vector<int> second = { 10, 20, 30, 40, 50 };

    // Result array
    int res[5];

    // std::transform applies std::minus to the whole array
    // std::transform(first, first + 5, second, res, std::minus<int>());
    std::transform(first.begin(), first.end(), second.begin(), res, std::minus<int>());

    std::vector<int> results(res, res + sizeof(res) / sizeof(res[0]));
    // Printing the result array
    for (int i = 0; i < 5; i++)
        std::cout << results[i] << " ";
    std::cout<<"\n";
    return 0;
}