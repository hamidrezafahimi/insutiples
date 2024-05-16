#include "Config.h"

int main() {
    ConfigHandle config = Config::GetInstance("path-to-yaml-file");
    return 0;
}