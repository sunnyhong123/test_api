import requests
from lxml import etree


url = 'http://24mail.chacuo.net/'
res = requests.get(url)
etr = etree.HTML(res.content)
a = etr.xpath('//input[@id="converts"]/@value')
print(a)