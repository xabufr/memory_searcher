import sys

from logic.tika import Tika


files = sys.argv[1:]


tika = Tika()
for file_name in files:
    print(tika.get_file_metadata(file_name))
