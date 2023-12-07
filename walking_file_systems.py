import os

TARGET_FOLDER = "."

SKIP = ".git"

def main():
    # find all Python scripts and display with their size
    for folder, subfolders, file_names in os.walk(TARGET_FOLDER):
        if SKIP in subfolders:
            subfolders.remove(SKIP)
        print(folder)
        for file_name in file_names:
            # any criteria here...
            if file_name.endswith('.py'):
                file_path = os.path.join(folder, file_name)
                # YOU CAN DO ANYTHING WITH THE FILE....
                file_size = os.path.getsize(file_path)
                print(f"     {file_size:10d} {file_name}")

main()
