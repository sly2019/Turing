import requests
from bs4 import BeautifulSoup
import re

url = "http://quote.eastmoney.com/stock_list.html#sh"

res = requests.get(url)
res.encoding = 'gb18030'
# print(res.text)

# 用 html.parser解析器解析demo(即 r.text),赋给soup
soup = BeautifulSoup(res.text, 'lxml')
print(soup.head.title.text)
slist_body = soup.find(name='div', attrs={"class": "quotebody"}).find_all('a', href=True)
i = 0
for stockBody in slist_body:
    # print(i)
    # print(stockBody.text, stockBody['href'])
    text = stockBody.text
    regex1 = r'(.*)\((.*)\)'
    matchObj = re.match(regex1, text, re.M | re.I)
    if matchObj:
        print(matchObj.group(1), matchObj.group(2), stockBody['href'])
    else:
        print('no match', stockBody)

