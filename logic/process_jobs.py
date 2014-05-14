from elasticsearch import Elasticsearch

from jobs import Jobs
from logic.tika import Tika


jobs = Jobs()
text_extractor = Tika()
es = Elasticsearch()
for job in jobs.iterate():
    es.index(index="memory", doc_type="pdf",
             body={"content": text_extractor.get_file_content(job), "metadata": text_extractor.get_file_metadata(job)})
