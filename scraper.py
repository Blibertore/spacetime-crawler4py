import re
from urllib.parse import urlparse, urldefrag
from bs4 import BeautifulSoup
import requests
import time


def scraper(url, resp):
    links = extract_next_links(url, resp)
    x = [link for link in links if is_valid(link)]
    for link in x:
        print(link)
    return [link for link in links if is_valid(link)]


def extract_next_links(url, resp):
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content
    html = requests.get(resp.url)
    data = html.text
    soup = BeautifulSoup(data, features="html.parser")
    url_set = set()
    for link in soup.find_all('a'):
        if resp.raw_response.content != None and resp.status == 200:
            try:
                url_set.add(urldefrag(link.get('href'))[0])
                time.sleep(1)
            except Exception:
                print("ERROR HERE")
                # url_set.add(link.get('href'))
                # time.sleep(5)
                pass
    return list(url_set)

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower()) and re.search(
            r".*\.(ics.uci.edu|cs.uci.edu|informatics.uci.edu|stat.uci.edu|today.uci.edu/department/information_computer_sciences)", parsed.netloc.lower())


    except TypeError:
        print ("TypeError for ", parsed)
        raise
