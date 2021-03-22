import os
from datetime import datetime


def generate_filename_with_timestamp(file):
    filename = file.name
    file_base_name = os.path.splitext(filename)[0]
    file_extension = os.path.splitext(filename)[1]
    milli_timestamp = int(datetime.now().timestamp() * 1000)
    return f'{file_base_name}_{milli_timestamp}{file_extension}'
