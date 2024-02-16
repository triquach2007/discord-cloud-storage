from typing import *
from constant import DB_PATH
import json

def new_file_entry(file_name:str, message_ids:List[int]):
    data = {
        "file_name": file_name,
        "message_ids": []
    }

    data["message_ids"].extend(message_ids)

    with open(DB_PATH, "r+") as f:
        d = json.load(f)
        d["files"].append(data)
        f.seek(0)
        json.dump(d, f, indent=4)

def load_entry(file_name):
    with open(DB_PATH, "r") as f:
        d = json.load(f)
    return list(filter(lambda file_dict: file_dict["file_name"] == file_name, d["files"]))[0]