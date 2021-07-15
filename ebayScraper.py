from sys import call_tracing
import requests
from bs4 import BeautifulSoup
import smtplib
import time

#define page and chosse
URL = 'https://www.ebay.com/itm/294241137953?epid=13041717342&_trkparms=ispr%3D1&hash=item4482237521:g:RuMAAOSwjLpg08Bb&amdata=enc%3AAQAGAAACgPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsS%252Fwocn770hnih0B3mVHNZ5P8u7iCUFZ470qHJD5GfeoN2QKBw6rYrdoMW7GwrZCh3SZiqt3h2rJSE6n5jANO9zQCXH4GzrDm7sxDDmMADm%252Fg5AhgrUw8JejCF5Q7r%252Bbxp1fBS1ahcyxjtcIcSyS5ll0T394n8ue39V8f3alKOIpylzcxf7u1QZh4GUX9y4z7hGSYg6LC3GaAdRNllWN%252FFv4ayuV2PSQ3du8Ee%252FNAYuyo%252B5W6Lz9tVpinezHdoVQWWtz3ntVyXTNo7oguluUfX3lIq%252F2RIBAlwUj7%252BLrtGJtIYl44%252BRKMAxxR3fT%252F2gYipVt14dFIdELTDjFu1zQtzcmbTcJjJTX1ZzFZ6Pscpj3WGgI%252BLP%252BY1pirMdIOo6cjhf%252FBDT5q2aJ343ewj2hTFFA7viTGCAvcKDiqJs4%252BS4EaszxK78eQZ7bVgWwmvgHjOAOlVwTe17O9oXcK06lGuD7BV5SsRcVQbHB9zrYtIbB9RNe48My%252F%252BgvwIOCfVxSDTnCejpg0bd%252BZdDbi0FF7%252BtYKK9YQdMABFCSEuDHIdbyZ0EAZmm1z%252Bk89JZgQ92nl7kxcARsuVgfqgHmeSgbZZR7CFjKDW4X40dtcWwW4zcbb%252FDQ2btC6L5%252BJwzCQH7vPAmXFnp2yeUshqglUOgtsNTHEILD82CaKn4b0J7HNAyGUPfI3%252F2db84OCN0GxenDCy3vNpIBX731xxf7Z4VfU9wLMSNkDGKiou8yq2UBdogUFTNbm768pgl5i%252FZDrDPv%252FM3MF8%252FHkXEO4nguxzfctxU2ier6nDs53L1bSx4CWOw4c%253D%7Campid%3APL_CLK%7Cclp%3A2334524'
header = {"User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=header)
    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum").get_text()

    conveted_price = float(price[4:])

    if(conveted_price< 600):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #login
    server.login('xxx@gmail.com', 'hrcubvrnzpnltsvb')

    subject = 'Price fell down!!'

    msg = f"Subject: {subject}\n\n Check this link: \n{URL}"

    server.sendmail(
        'Automation bot :-)',
        'XXX@gmail.com',
        msg
    )
    print("Hey!!!! EMAIL HAS BEEN SENT!!")

    server.quit()
    

while(True):
    check_price()
    time.sleep(60*60*24)

