from elasticsearch import Elasticsearch


class MemorySearcher:
    def __init__(self, index="memory"):
        self.__es = Elasticsearch()
        self.__index = index
        self.__type = "pdf"

    def __search(self, query):
        return self.__es.search(index=self.__index, doc_type=self.__type, body=query)

    def search_globally(self, sentences, result_fields=None):
        query = {
            'query': {
                'query_string': {
                    'query': '_all:"' + sentences.replace('"', '\\"') + '"'
                }
            }
        }
        if result_fields:
            query['fields'] = result_fields
        return self.__search(query)

    def search_on_fields(self, terms):
        match = []
        query = {'query': match}
        for arg in terms.keys():
            match.append({
                'term': {
                    arg: terms[arg]
                }
            })
        return self.__search(query)

    def suggest_search(self, query):
        pass

    def index(self, content, metadata):
        self.__es.create(self.__index, self.__type, {'content': content, 'metadata': metadata})

    def __set_mapping(self):
        pass


if __name__ == "__main__":
    searcher = MemorySearcher()
    #print(searcher.search_on_fields({'metadata.Content-Length': 434010, 'creator': 'Campagne'}))
    print(searcher.search_globally('Campagne', ['metadata.title']))
