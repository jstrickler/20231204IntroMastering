import os

DIRECTORY = '../DATA'

for entry_name in sorted(os.listdir(DIRECTORY)):
    file_path = os.path.join(DIRECTORY, entry_name)
    file_size = os.path.getsize(file_path)
    print(f"{entry_name:30s} {file_size:10d}")
print('-' * 60)
print(f"os.listdir(DIRECTORY): {os.listdir(DIRECTORY)}")


