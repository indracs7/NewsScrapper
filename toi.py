from urllib.request import urlopen
import pandas as pd
def getListOfUrls():
    from bs4 import BeautifulSoup as soup
    url = "https://timesofindia.indiatimes.com/topic/Kolkata-Accident-"
    url2 = "https://timesofindia.indiatimes.com"
    html = urlopen(url)
    soup = soup(html, 'lxml')
    table = soup.find_all('span', {'class': 'fb'})
    print(len(table))
    list_url = []
    for row in table:
        list_url.append(url2+row['data-url'])
    print(list_url)
    return list_url
    #end of websites url
    #print(soup.prettify())
def getData():
    list_url = getListOfUrls()
    content = []
    time = []
    for link in list_url:
        from bs4 import BeautifulSoup as soup
        print(link)
        html2 = urlopen(link)
        #print(soup.prettify())
        soup = soup(html2, 'lxml')
        #print(soup.get_text)
        temp = soup.find_all('div', {'class': 'Normal'}, True)[0].text
        content.append(temp.strip().replace('\n', ''))
        time.append(soup.find('time')['datetime'])

    return content,time
    #print(content)
def makeCSV():
    content, time = getData()
    dict = {'Time': time, 'Source':'Times of India', 'Content': content}
    df = pd.DataFrame(dict)
    df.to_csv('./res/TOI.csv')
makeCSV()
