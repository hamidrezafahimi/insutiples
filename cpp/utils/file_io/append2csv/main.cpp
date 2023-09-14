#include <fstream>
#include <vector>
// #include <boost>

int main ()
{
    // std::ofstream file( "table.csv", std::ios::app );
    // file.open ("output.csv");
    // file << "a" << "," << "b" << "," << "c";

    std::vector<int> SMA{1,2,3,4,5};

    // if(!boost::filesystem::exists("./CalculatedOutput/SMAcurrent.csv"))
    // {
        std::ofstream SMAfile;
        SMAfile.open("./CalculatedOutput/SMAcurrent.csv", std::ios::app);
        SMAfile << "SMA" << '\n' << SMA[0] << '\n';
        SMAfile.close();
    // }
    // else
    // {
        std::ofstream SMARfile("./CalculatedOutput1/SMAReplacecurrent.csv");
        std::ifstream SMAfile1("./CalculatedOutput1/SMAcurrent.csv");

        // // first read header from input file

        std::string header;
        std::getline(SMAfile1, header);

        // // Next write out the header followed by the new data
        // // then everything else

        // SMARfile << header << '\n';  // Writing header
        // SMARfile << SMA[0] << '\n';  // Write new data after header
        // SMARfile << SMAfile.rdbuf(); // Write rest of data

        // SMAfile.close();
        // SMARfile.close();
        // std::remove("./CalculatedOutput/SMAcurrent.csv");
        // std::rename("./CalculatedOutput/SMAReplacecurrent.csv",
        //     "./CalculatedOutput/SMAcurrent.csv");
    // }
}