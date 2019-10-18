# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen
# import pandas as pd
# url = "https://timesofindia.indiatimes.com/city/kolkata/youth-in-car-chased-and-robbed-during-immersion-at-naktala/articleshow/71574681.cms"
# html = urlopen(url)
# soup = soup(html, 'lxml')
# #print(soup.prettify())
# content = []
# temp = soup.find_all('div', {'class': 'Normal'}, True)[0].text
# content.append(temp.strip().replace('\n', ''))
# print(content)
import pandas as pd
filenames = ['TOI','NDTV','Kolkata24*7']
df2 = []
for f in filenames:
    df = pd.read_csv("./res/"+f+".csv")
    df = df[df.columns[1:]]
    df2.append(df)
combined_csv = pd.concat(df2)
combined_csv.to_csv( "./res/combined_csv.csv", index=False, encoding='utf-8-sig')
l = [x for x in range(1, 192)]
df = pd.read_csv("./res/combined_csv.csv")
#print(len(df['Time']))
df.insert(0,"Index",l )
df.to_csv('./res/AccidentReport.csv',index=False, encoding='utf-8-sig')