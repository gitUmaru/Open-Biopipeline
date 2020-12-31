from webscrape import scrape
import urllib.parse
import urllib.request

class Uniprot():
    '''
    TODO: Add class and method documentation
    '''
    def __init__(self,gene_name=None,gene_entry=None,organism="HUMAN"):
        self.__gene_entry = gene_entry
        self.__gene_name = gene_name
        self.__organism = organism


    def protein_entries(self):
        data = urllib.parse.urlencode({
            'from': 'GENENAME',
            'to': 'ID',
            'format': 'list',
            'query': self.__gene_name,
            }).encode('utf-8')

        req = urllib.request.Request('https://www.uniprot.org/uploadlists/', data)
        with urllib.request.urlopen(req) as f:
           response = f.read()
        return [r for r in response.decode('utf-8').split() if self.__organism in r]

    def protein_function(self):
        '''TODO: Override this webscrape with uniprot API support'''
        items = scrape('https://www.uniprot.org/uniprot/'+self.__gene_entry,'span')
        return str(items[46])[22:str(items[46]).find('<span class="attribution')]


    def protein_AASeq(self):
        '''TODO: Override this webscrape with uniprot API support'''
        items = scrape('https://www.uniprot.org/uniprot/'+self.__gene_entry,'span')
        return items[29].string


if __name__ == '__main__':
    up = Uniprot('VEGFA')
    print(up.protein_entries())
