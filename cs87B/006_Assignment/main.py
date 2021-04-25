import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse

import pprint
pp = pprint.PrettyPrinter(indent=4)

def googleSearch(query):
    URLS = [ ] 
    
    url = f"https://google.com/search?q={query}"
    try:
            html = requests.get(url)
            if html.status_code==200:
                soup = BeautifulSoup(html.text, 'lxml')
                a = soup.find_all('a')
                for anchor in a:
                    k = anchor.get('href')
                    try:
                        m = re.search("(?P<url>https?://[^\s]+)", k)
                        n = m.group(0)
                        rul = n.split('&')[0]
                        domain = urlparse(rul)
                        if(re.search('google.com', domain.netloc)):
                            continue
                        else:
                            URLS.append(rul)
                    except:
                        continue
    except Exception as ex:
            print(str(ex))
    finally:
            return URLS



def main():
    keyword = input("Enter seach keyword: ")
    pp.pprint(googleSearch(keyword))


if __name__=="__main__": main()


"""
Sample run: 
➜  006_Assignment git:(nndata) ✗ python3 main.py  
Enter seach keyword: react.js 
[   'https://reactjs.org/',
    'https://reactjs.org/tutorial/tutorial.html',
    'https://reactjs.org/docs/getting-started.html',
    'https://reactjs.org/docs/hello-world.html',
    'https://reactjs.org/docs/create-a-new-react-app.html',
    'https://reactjs.org/docs/hooks-intro.html',
    'https://reactjs.org/docs/react-api.html',
    'https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg',
    'https://reactjs.org/logo-og.png',
    'https://i.ytimg.com/vi/JPT3bFIwJYA/maxresdefault.jpg',
    'https://peerbits-wpengine.netdna-ssl.com/wp-content/uploads/2019/09/the-benefits-of-reactjs-main.jpg',
    'https://en.wikipedia.org/wiki/React_(JavaScript_library)',
    'https://en.wikipedia.org/wiki/React_(JavaScript_library)',
    'https://en.wikipedia.org/wiki/React_(JavaScript_library)%23Notable_features',
    'https://en.wikipedia.org/wiki/React_(JavaScript_library)%23JSX',
    'https://en.wikipedia.org/wiki/React_(JavaScript_library)%23React_hooks',
    'https://en.wikipedia.org/wiki/React_(JavaScript_library)%23Common_idioms',
    'https://en.wikipedia.org/wiki/Facebook',
    'https://en.wikipedia.org/wiki/JavaScript',
    'https://en.wikipedia.org/wiki/Web_platform',
    'https://www.youtube.com/watch%3Fv%3Dw7ejDZ8SWv8',
    'https://www.youtube.com/watch%3Fv%3Dw7ejDZ8SWv8',
    'https://github.com/facebook/react',
    'https://www.w3schools.com/react/',
    'https://www.w3schools.com/whatis/whatis_react.asp',
    'https://spring.io/guides/tutorials/react-and-spring-data-rest/']

"""