#include<iostream>
#define stringify( name ) #name
// using namespace std;

enum Color { RED = 2, BLUE = 4, GREEN = 8 };



int main(){
    Color color = Color::RED;
    auto color_name = magic_enum::enum_name(color);
    // color_name -> "RED"

    std::string color_name{"GREEN"};
    auto color = magic_enum::enum_cast<Color>(color_name);
    if (color.has_value()) {
        std::cout<<"df\n";
    // color.value() -> Color::GREEN
    }
    return 0;
}