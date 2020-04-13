from webscrape import scrape

def protein_entry(gene_name):
    genes = []
    genes_entry = []
    items = scrape('https://www.uniprot.org/uniprot/?query="'+gene_name+'+human"+AND+organism%3A%22Homo+sapiens+%28Human%29+%5B9606%5D%22&sort=score','a')

    for i in range(len(items)):

        if '<a href="/uniprot/?query=' in str(items[i]):
            items[i] = "NULL"

        if '<a href="/uniprot/' in str(items[i]):
            genes.append(str(items[i]))

    for i in range(len(genes)):
        genes_entry.append(genes[i][26:32])

    return genes_entry, genes

def protein_function(gene_entry):
    items = scrape('https://www.uniprot.org/uniprot/'+gene_entry,'span')
    return str(items[46])[22:str(items[46]).find('<span class="attribution')]


def protein_AASeq(gene_entry):
    items = scrape('https://www.uniprot.org/uniprot/'+gene_entry,'span')
    return items[29].string


if __name__ == '__main__':
    pass
