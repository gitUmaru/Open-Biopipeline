import urllib.request

def get_atlas_xml(gene):
    urllib.request.urlretrieve('https://www.proteinatlas.org/search/'+gene+'?format=xml','xml/protein_atlas/'+gene+"_protein_atlas_data.xml")

if __name__ == '__main__':
    get_atlas_xml('VEGFA')
