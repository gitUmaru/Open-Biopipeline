from webscrape import scrape
import urllib.request
import os

class GeneNameError(Exception):
    '''Exception raised for errors in Gene Name.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    '''
    def __init__(self,expression,message):
        self._expression = expression
        self._message = message

class Kegg():
    '''
    TODO: Add class documentation and methods
    '''
    def __init__(self,gene_id=None,protein_name=None,ncbi_id=None):
        self.__gene_id = gene_id
        self.__ncbi_id = ncbi_id
        self.__protein_name = None

    def convert_ncbi_to_kegg(self,ncbi_id=None):
        if(ncbi_id is not None):
            self.__ncbi_id = ncbi_id
            req = urllib.request.Request(f'http://rest.kegg.jp/conv/genes/ncbi-geneid:{self.__ncbi_id}')
            with urllib.request.urlopen(req) as f:
               response = f.read()
            return response.decode().split()

    def get_pathway_image(self,protein_name=None):
        if(self.__protein_name is None):
            self.__protein_name = protein_name
        if(self.__protein_name is not None):
            items = scrape('https://www.kegg.jp/kegg-bin/search_pathway_text?map=map&keyword='+self.__protein_name+'&mode=1&viewImage=true','img')
            url_ext = []
            for i in range(len(items)):
                url_ext.append(items[i].parent['href'])

            images = scrape('https://www.kegg.jp'+url_ext[0],'img')

            urllib.request.urlretrieve('https://www.kegg.jp'+images[2]['src'], self.__protein_name+"_pathway.jpg")

            return 'https://www.kegg.jp'+images[2]['src']
        else:
            GeneNameError(self.__protein_name,"There is no specified protein name")

def main():
    kegg = Kegg()
    print(kegg.convert_ncbi_to_kegg('944753'))

if __name__ == '__main__':
    main()
