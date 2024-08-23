from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from datetime import datetime
from songline import Sendline

token = 'wvhDCchPuRjD5ewWMZJi2txj0gJh98Oz8uKFM3OJ83s'

messenger = Sendline(token)

now = datetime.now()

url = "https://www.caltex.com/th/motorists/products-and-services/fuel-prices.html"

webopen = req(url)
page_html = webopen.read()
webopen.close()

data = soup(page_html,'html.parser')

oil_name = data.find_all('div',{'class':'col-xs-4 col-md-6 first-col'})
oil_price = data.find_all('div',{'class':'col-xs-4 col-md-3'})

for name , price in zip(oil_name[1:],oil_price[1:]):
    name = name.text
    name =name.replace('\n','')
    txt_price = price.text
    txt_price = txt_price.replace('\n','')
    time = now.strftime("%H:%M:%S")
    messenger.sendtext(f"ราคาน้ำมันวันนี้ \n{name} \nราคาน้ำมันต่อลิตร : {txt_price} \nเวลา {time}")