from Jobs import Jobs
from TextExtractor import TextExtractor

jobs = Jobs()
text_extractor = TextExtractor()
for job in jobs.iterate():
    print(text_extractor.extract_text(job))
