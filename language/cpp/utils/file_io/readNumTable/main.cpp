#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

int main()
{
    std::vector<std::vector<float>> data;
    std::ifstream input( "test.csv" );
    int i = 0;
    for( std::string line; getline( input, line ); )
    {
        data.push_back(std::vector<float>());
        std::istringstream iss(line);
        std::string num;
        while(std::getline(iss, num, ','))
        {
            data[i].push_back(stof(num));
        }
        i++;
    }

    for (auto& row: data)
    {
        for(auto& num: row)
            std::cout<<num<<"\t";
        std::cout<<"\n";
    }
}