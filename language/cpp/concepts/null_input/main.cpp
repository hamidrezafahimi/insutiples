#include <iostream>

using namespace std;

void func(void *p)
{
if (p == nullptr)
	std::cout<<"hi\n";
else
	std::cout<<"ho\n";
}

int main(){

func(nullptr);
return 0;

}
