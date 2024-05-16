#ifndef CONFIG_H_
#define CONFIG_H_

#include <string>
#include <iostream>

void throwRequestWhileNotSet(std::string inp) {
    throw std::invalid_argument(std::string("Request for parameter '") + \
        inp + "'while not set");
}

void throwUnableToLoad(std::string p) {
    throw std::invalid_argument(std::string("Unable to load parameter '") + \
        p + "'");
}

typedef std::shared_ptr<Config> ConfigHandle;

class Config {
public:
    static ConfigHandle GetInstance(std::string = "");

private:
    Config(std::string = "");

    static ConfigHandle handle;

    YAML::Node mainNode;

    std::string inputType = types::InputType::NONE;
    int tag = types::INF_F;
    float ratio = types::INF_F;
    double value = types::INF_F;

    typename t
    void setField(t& field, std::string key) {
        if (mainNode[key]) {
            try {
                field = mainNode[key].as<t>();
            } catch (...) {
                throwUnableToLoad(key)
            }
        }
    }
}

#endif