import xml.etree.ElementTree as ET
from Bio import Entrez


def parse():
    root = ET.parse('my_blast.xml').getroot()

    print(root[8][0][1].text)

    for i in range(len(root)):
        print(i, root[i].tag,"||    " + root[i].text)

    gene_id = root[5].text


    print(gene_id)


if __name__ == '__main__':
    parse()
