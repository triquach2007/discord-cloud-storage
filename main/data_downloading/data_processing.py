from constant import DOWNLOAD_PATH
import os

def join_data():
    data = b''
    for file in os.listdir("main/download_buffer/"):
        with open(os.path.join("main/download_buffer/", file), "rb") as f:
            data += f.read()
    return data

def download_file(file_name, data):
    with open(os.path.join(DOWNLOAD_PATH, file_name), "wb") as f:
        f.write(data)

def delete_file_in_download_buffer() -> None:
    for file in os.listdir("main/download_buffer"):
        os.remove(os.path.join("main/download_buffer", file))