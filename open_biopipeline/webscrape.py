from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):

    ## It trys to get content of url by sending HTML GET
    ## if(content == XML || HTML){return content}else{return None}

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    ## if (response == HTML){return True}else{return False}
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    ## this would be intuitive if you were smart
    ## lowkey common sense
    print(e)


def scrape(url,element):
    items = []
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    for a in html.find_all(element, attrs={}):
        #print(a)
        items.append(a)
    return items

if __name__ == '__main__':
    gene_name = 'NF1'
    items = scrape('https://www.uniprot.org/uniprot/?query='+gene_name+'+AND+organism%3A%22Homo+sapiens+%28Human%29+%5B9606%5D%22&sort=score','a')
