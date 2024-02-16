from typing import *
from constant import CHUCK
import os

def load_up_files() -> Generator:
    return [os.path.join("main/upload_buffer", file) for file in os.listdir(f"main/upload_buffer/")]

def delete_file_in_upload_buffer(file:str) -> None:
    os.remove(os.path.join("main/upload_buffer", file))

def split_up_file(file:str) -> Generator:
    with open(file, "rb") as f:
        while data:=f.read(CHUCK):
            yield data