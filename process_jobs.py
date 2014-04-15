from Jobs import Jobs
from tika import Tika

jobs = Jobs()
text_extractor = Tika()
for job in jobs.iterate():
    print(text_extractor.get_file_content(job))
