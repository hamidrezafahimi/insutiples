#include "SampleClass.h"


SampleClass::SampleClass(std::string txt)
{
	a = txt;
}


void SampleClass::samplePublicFunc(int n)
{
	std::cout<<a<<"\n";
}


void SampleClass::samplePrivateFunc(double d)
{

}


float SampleClass::calcDist(std::vector<float> &vc)
{
	return 0;
}
