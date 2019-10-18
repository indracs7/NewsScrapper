import re
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup as soup
city = ['Kolkata:', 'Nadia:', 'Howrah:', 'Barrackpore:', 'Bidhannagar:']
def getLinks():
    url2 = "https://english.kolkata24x7.com/?s=road+accident+kolkata"
    url3 = "https://english.kolkata24x7.com/page/4/?s=road+accident+kolkata"
    main_url = "https://english.kolkata24x7.com/"
    end_url = "?s=road+accident+kolkata"
    links = []
    for i in range(1,13,1):
        if(i == 1):
            url = main_url+end_url
        else:
            url = main_url+"page/"+str(i)+"/"+end_url
        soup = getSoup(url)
        table = soup.find_all('a', {'rel': 'bookmark'})
        for row in table:
            try:
                if row.img['height'] == '100':
                    links.append(row['href'])
                    #print(row['href'])
            except:
                pass
    return links
def getData():
    content = []
    time = []
    links = getLinks()
    for link in links:
        soup = getSoup(link)
        print(link)
        [s.extract() for s in soup('script')]
        #print(soup.prettify())
        temp = soup.find_all('div', {'class': 'td-post-content'}, True)[0].text
        temp = re.sub("\s\s+", " ", temp)
        temp = temp.strip().replace('\r', '').replace('\n', '')
        flag = False
        for c in city:
            if(c in temp ):
                flag = True
                break
        if not flag:
            continue
        content.append(temp)
        print(temp)
        time.append(soup.find('time')['datetime'])

    return content, time


def getSoup(url):
    from bs4 import BeautifulSoup as soup
    html = urlopen(url)
    soup = soup(html, 'lxml')
    return soup
def makeCSV():
    content, time = getData()
    dict = {'Time': time, 'Source':'Kolkata24*7', 'Content': content}
    df = pd.DataFrame(dict)
    df.to_csv('./res/Kolkata24*7.csv')
makeCSV()

