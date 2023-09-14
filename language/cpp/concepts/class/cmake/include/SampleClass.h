#ifndef SAMPLECLASS_H
#define SAMPLECLASS_H

#include <iostream>
#include <vector>


class SampleClass {

public:

    bool flag = false;
    std::string a = "12";

    SampleClass(std::string);
    void samplePublicFunc(int);

private:

    std::vector<std::vector<float>> vec;
    int b = 0;
    float l = 0.1;

    float calcDist(std::vector<float> &);
    void samplePrivateFunc(double);
};


#endif
