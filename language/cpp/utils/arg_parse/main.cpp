#include <iostream>

int main(int argc, char* argv[])
{
    // Check the number of parameters
    std::cout<<argc<<"\n";
    if (argc < 2) {
        // Tell the user how to run the program
        std::cerr << "Usage: " << argv[0] << " Q_FILE_NAME" << std::endl;
        /* "Usage messages" are a conventional way of telling the user
         * how to run a program if they enter the command incorrectly.
         */
        return 1;
    }
    // Print the user's name:
    std::string name = argv[1];
    int a = atoi(argv[2]);
    int b = atoi(argv[3]);
    std::cout << argv[0] << "says hello, " << name << "!" << std::endl;
    std::cout <<  a+b << std::endl;
    return 0;
}