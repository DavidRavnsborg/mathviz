from typing import List, Dict, Any
import hashlib
import json


def input_expression_hash(input_expressions: List[Dict]) -> str:
    """Pre-processing to make input_expressions JSON serializable."""
    print(input_expressions)
    for input in input_expressions:
        input["type"] = int(input["type"])
    return list_hash(input_expressions)


def list_hash(data_list: List[Dict]) -> str:
    """MD5 hash of a dictionary."""
    print(data_list)
    dhash = hashlib.md5()
    encoded = json.dumps(data_list, sort_keys=True).encode()
    dhash.update(encoded)
    return dhash.hexdigest()
