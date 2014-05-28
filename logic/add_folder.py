import sys
import os

from jobs import Jobs


folders = sys.argv[1:]
jobs = Jobs()

for folder in folders:
    files_names = os.listdir(folder)
    files = [os.path.join(folder, file_name) for file_name in files_names if os.path.splitext(file_name)[1] == ".pdf"]
    for file_path in files:
        jobs.add_job(file_path)
