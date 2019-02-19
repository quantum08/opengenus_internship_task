from bs4 import BeautifulSoup
from urllib.request import urlopen


#function to get web page size

def web_html_page_size(url):
    page_content = urlopen(url).read()
    page_size = len(page_content)

    return page_size


#function to get all link count for same domain
def link_count(url):

    same_domain_links = 0
    
    url_domain = url.split('/')[2]

    page = urlopen(url).read()

    page_content = BeautifulSoup(page, features="lxml")

    for link in page_content.find_all('a'):
        if link.has_attr('href'):
            link_url = link.attrs['href']
        try:
            link_url_domain = link_url.split('/')[2]

            if url_domain in link_url_domain:
                same_domain_links+=1
        except:
            pass

    return same_domain_links



if __name__ == "__main__":

    #input url from user 
    url_link =input("Enter  the url ")

    #check for http and adding http in the url if not present there
    if url_link[:4] != 'http':
        url_link = 'http://' + url_link

    web_page_size = web_html_page_size(url_link)
    same_domain_links = link_count(url_link)

    print ('Page Size is :-  ', web_page_size , ' Bytes')
    print ('Number of links to same domain is :- ', same_domain_links)
