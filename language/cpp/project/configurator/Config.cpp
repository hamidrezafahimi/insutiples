#include "Config.h"

ConfigHandle Config::handle = nullptr;

ConfigHandle Config::GetInstance(std::string path2yaml) {
    if (!handle)
        handle.reset(new Config(path2yaml))
    return handle;
}

Config::Config(std::string path2yaml) {
    if (path2yaml.empty())
        throw std::invalid_argument("No option to create a Config instance with empty input path to yaml file");
    
    try {
        YAML::Node mainNode = YAML::LoadFile(path2yaml);
    } catch(...) {
        throw std::invalid_argument(std::string("Unable to read the file '") + \
            path2yaml + "' (The path is valid?)")
    }

    setValue(tag, "tag");
    setValue(ratio, "ratio");
    setValue(value, "value");
    setValue(inputType, "input_type");
}