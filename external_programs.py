from subprocess import run, PIPE, CalledProcessError
import shlex
import os

full_command = "netstat -an"

command_words = shlex.split(full_command)

# could use glob to expand wildcards

print(f"command_words: {command_words}")

process = run(command_words, stdout=PIPE)

output_lines = process.stdout.decode().splitlines()

for line in output_lines:
    if "ESTABLISHED" in line:
        print(line)

proc = run(shlex.split("ls -l"), stdout=PIPE)
lines = proc.stdout.decode().splitlines()
py_files = [f for f in lines if f.endswith('py')]
for py_file in py_files:
    print(py_file)
print('-' * 60)

for py_file in py_files:
    fields = py_file.split()
    if len(fields) < 5:
        continue
    perm, links, owner, group, size, *_ = fields
    file_size = int(size)
    
    if file_size > 1000:
        print(py_file)
print('-' * 60)

for entry in os.scandir('.'):
    if entry.name.endswith('py'):
        file_size = entry.stat().st_size
        if file_size > 1000:
            print(f"{entry.name:20} {file_size}")