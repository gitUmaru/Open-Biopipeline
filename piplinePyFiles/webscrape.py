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


def scrape():
    raw_html = simple_get('https://www.ncbi.nlm.nih.gov/nuccore/AH002844.2')
    html = BeautifulSoup(raw_html, 'html.parser')
    for i in html.find_all('div', attrs={}):
            print(i)

if __name__ = '__main__':
    scrape()
