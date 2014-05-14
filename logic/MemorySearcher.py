from elasticsearch import Elasticsearch


class MemorySearcher:
    def __init__(self):
        self.__es = Elasticsearch()

    def global_search(self, query):
        return self.__es.search(index="memory", doc_type="pdf", body=query)

    def search_on_fields(self, **kwargs):
        pass

    def suggest_search(self, query):
        pass

    def index(self, content, metadata):
        pass

    def __set_mapping(self):
        pass

if __name__ == "__main__":
    searcher = MemorySearcher()
    print("coucou")
    print(searcher.global_search({"query": {"match": {"_all": "Cluster de Supervision"}}}))