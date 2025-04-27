from bs4 import BeautifulSoup
import requests
import pprint
import os
from dotenv import load_dotenv, find_dotenv
import smtplib

load_dotenv(find_dotenv())

SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_KEY = os.getenv("GMAIL_KEY")
TO_ADDRESS = os.getenv("TO_ADDRESS")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-IE,en-US;q=0.9,en;q=0.8,pl;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
  }

URL = "https://www.amazon.co.uk/Metal-Gear-Solid-Master-Collection/dp/B0C94GXF3N/ref=sr_1_2?crid=J8M3PLARBFES&dib=eyJ2IjoiMSJ9.X09Cr8MSjWIJIc91RSp0b0IhdED6Pg3ROjyan2zb4p6F7hQAVvo5eDDFsXyRuZW8AZfTsw6BtLyL_gULqtka6P2GJ3eLrphJ4XwxgemKONW2gfgpFldXWKiIqdOUth8Qxp_6cnJRavC8tOYwol6Fekkglv9M4VXtYTCwl9Xazj4sA3U6ENjJzPoYP3i4mbiH7LYBg6sGwOTqvE4Qk-gg0coPvr3suUzFZeeNvgEjs6I.D3G3jC7p-7kqGiDQZ1G6j-vT9eIqG6XmhaMmYV2Kmvc&dib_tag=se&keywords=metal%2Bgear%2Bsolid%2Bmaster%2Bcollection&nsdOptOutParam=true&qid=1734448294&s=videogames&sprefix=metal%2Bgear%2Bsolid%2Bmaster%2Cvideogames%2C74&sr=1-2&th=1"

response = requests.get(url=URL, headers=headers)
raw_html = response.text

soup = BeautifulSoup(raw_html, "html.parser")

raw_price = soup.find(name="span", class_="aok-offscreen").get_text().split(" ")[3]
price = float(raw_price.split("£")[1])

print(price)

product_name = " ".join(soup.find(class_="a-size-large product-title-word-break").get_text().split())
product_name.encode('utf-8')
print(product_name)
message = f"Subject:Amazon Price Alert!\n\n{product_name} is now £{price}\n{URL}".encode("utf-8")

if price < 100:
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(user=GMAIL_ADDRESS, password=GMAIL_KEY)
        connection.sendmail(from_addr=GMAIL_ADDRESS,
                            to_addrs=TO_ADDRESS,
                            msg=message)

