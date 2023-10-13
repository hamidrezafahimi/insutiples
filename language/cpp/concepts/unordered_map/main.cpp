#include <iostream>
#include <unordered_map>
#include <vector>

class AutoPlayer {
public:
    AutoPlayer(int a, std::string n) {
        num = a;
        name = n;
    }

    std::string name = "";

    private:
        int num = 0;
};

int main() {

    AutoPlayer *ap1 = new AutoPlayer(1, "edr");
    AutoPlayer *ap2 = new AutoPlayer(2, "eas");
    AutoPlayer *ap3 = new AutoPlayer(3, "esd");

    std::vector<AutoPlayer*> aps = {ap1, ap2, ap3};

    std::unordered_map<std::string, AutoPlayer*> minds;

    int l = aps.size();
    for (int k = 0; k < l; k++) {
        std::cout<<"er1\n";
        minds[aps[k]->name] = aps[k];
    }

    return 0;

}