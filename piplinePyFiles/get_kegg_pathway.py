from webscrape import scrape
import urllib.request

def get_pathway(protein_name):
    items = scrape('https://www.kegg.jp/kegg-bin/search_pathway_text?map=map&keyword='+protein_name+'&mode=1&viewImage=true','img')
    url_ext = []
    for i in range(len(items)):
        #print(i,items[i])
        url_ext.append(items[i].parent['href'])
        #print(url_ext[i])

    images = scrape('https://www.kegg.jp'+url_ext[0],'img')

    urllib.request.urlretrieve('https://www.kegg.jp'+images[2]['src'], 'pathway_img/'+protein_name+"_pathway.jpg")

    return 'https://www.kegg.jp'+images[2]['src']

if __name__ == '__main__':
    print(get_pathway('BRCA1'))
