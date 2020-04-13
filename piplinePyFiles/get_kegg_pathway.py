from webscrape import *

def get_pathway(protein_name):
    items = scrape('https://www.kegg.jp/kegg-bin/search_pathway_text?map=map&keyword='+protein_name+'&mode=1&viewImage=true','img')
    url_ext = []
    for i in range(len(items)):
        #print(i,items[i])
        url_ext.append(items[i].parent['href'])
        #print(url_ext[i])

    images = scrape('https://www.kegg.jp'+url_ext[0],'img')


    return 'https://www.kegg.jp'+images[2]['src']

if __name__ == '__main__':
    print(get_pathway('VEGFA'))
