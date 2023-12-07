import os 
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

def main():
    file_path = os.path.join(FOLDER, FILE_NAME)
    file_size = os.path.getsize(file_path)
    print(f"file_size: {file_size}")

    raw_ts = os.path.getmtime(file_path)  # returns Unix epoch time (#seconds)
    file_ts = datetime.fromtimestamp(raw_ts)
    print(f"file_ts: {file_ts}")
    
    raw_ts = os.path.getatime(file_path)  # returns Unix epoch time (#seconds)
    file_ts = datetime.fromtimestamp(raw_ts)
    print(f"file_ts: {file_ts}")

    print(f"os.getcwd(): {os.getcwd()}")
    

main()


