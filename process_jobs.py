from jobs import Jobs
from tika import Tika
from elasticsearch import Elasticsearch

jobs = Jobs()
text_extractor = Tika()
es = Elasticsearch()
for job in jobs.iterate():
    es.index(index="memory", doc_type="pdf",
             body={"content": text_extractor.get_file_content(job), "metadata": text_extractor.get_file_metadata(job)})
