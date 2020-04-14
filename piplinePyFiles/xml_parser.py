import xml.etree.ElementTree as ET
from Bio import Entrez


def blast_parser(xml_file):
    root = ET.parse(xml_file).getroot()

    print(root[8][0][1].text)

    for i in range(len(root)):
        print(i, root[i].tag,"||    " + root[i].text)

    gene_id = root[5].text


    print(gene_id)

def protein_atlas_parser(xml_file):
    root = ET.parse(xml_file).getroot()

    for i in range(len(root)):
        try:
            prot_name = root[i][0].text
            tissue_expr = root[i][20][3][0].text
            desc = root[i][7][1].get('description')
            path_expr =  root[i][8][0].text
        except:
            print("\nAn error has been thrown, please handle\n")

        print(i,'Protein Name:', prot_name,'\n  Tissue expression summary: ',tissue_expr,'\n  Description: ',desc,'\n  RNA Cancer Specificity:', path_expr)

def print_xml_struct(xml_file):
    root = ET.parse(xml_file).getroot()
    print(root.tag)
    for i in range(len(root)):
        print(i,root[i])
        for j in range(len(root[i])):
            print(i,j,root[i][j])
            try:
                for k in range(len(root[i][j])):
                    print(i,j,k,root[i][j][k])
            except:
                print("\nThe index has left the bound, items dont exist\n")


if __name__ == '__main__':
    protein_atlas_parser('xml/protein_atlas/VEGFA_protein_atlas_data.xml')
