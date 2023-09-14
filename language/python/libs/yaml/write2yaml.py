
import sys
sys.path.insert(1, "../modules")

pp = "." # give it a directory to work in

from ruamel.yaml import YAML
from pathlib import Path

yaml = YAML()
path = Path(pp + "/EnvConfig.yaml")

from ruamel.yaml.main import \
    round_trip_load as yaml_load, \
    round_trip_dump as yaml_dump

# Yaml commentary
from ruamel.yaml.comments import \
    CommentedMap as OrderedDict, \
    CommentedSeq as OrderedList


shopping_list = OrderedDict({
    "Env Config": OrderedDict({
            "type": "free range",
            "brand": "Mr Tweedy",
            "amount": 12
        }),
    "Solver Config": OrderedDict({
        "type": "pasteurised",
        "litres": 1.5,
    })
    })
print(yaml_dump(shopping_list))


yaml.dump(shopping_list, path)