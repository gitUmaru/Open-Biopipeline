import urllib.request

class ProteinAtlas():
    '''
    Add class and method documentation plus incorperate parsers IN class
    '''
    def __init__(self):
        pass
    def get_atlas_xml(self,gene):
        urllib.request.urlretrieve('https://www.proteinatlas.org/search/'+gene+'?format=xml',gene+"_protein_atlas_data.xml")

if __name__ == '__main__':
    pa = ProteinAtlas()
    print(pa.get_atlas_xml('VEGFA'))
