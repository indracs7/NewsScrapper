import re
from urllib.request import urlopen,Request
import pandas as pd
def getLinks():
    url = "https://www.ndtv.com/topic/kolkata-accident"
    soup = getSoup(url)
    content = soup.find_all('p', {'class': 'header fbld'})
    links = []
    for c in content:
        links.append(c.a['href'])
    links = list(dict.fromkeys(links))
    #print(len(links))
    return links
def getData():
    content = []
    time = []
    links = getLinks()
    for url in links:
        print(url)
        soup = getSoup(url)
        #print(soup.prettify())
        time.append(soup.find('span', {'itemprop': 'dateModified'})['content'])
        temp = soup.find_all('div', {'class': 'ins_storybody'}, True)[0].text
        temp = temp.strip().replace('\r', '').replace('\n', '')
        inty = temp.index('Follow NDTV for')
        temp = temp[:inty]
        temp = temp.replace('googletag.cmd.push(function() { googletag.display("adslotNativeVideo"); });','')
        temp  = re.sub("\s\s+", " ", temp)
        content.append(temp)

        #print(temp)
    return content, time
def getSoup(url):
    from bs4 import BeautifulSoup as soup
    request = Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
    response = urlopen(request).read()
    soup = soup(response, 'lxml')
    return soup
def makeCSV():
    content, time = getData()
    dict = {'Time': time, 'Source':'NDTV', 'Content': content}
    df = pd.DataFrame(dict)
    df.to_csv('./res/NDTV.csv')
makeCSV()








