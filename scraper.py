import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.ae/Apple-MWP22ZE-A-AirPods-Pro/dp/B07ZQC2G9X/ref=sr_1_1_sspa?dchild=1&keywords=apple+airpods+pro&qid=1626240693&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRTkE4NzRYTFJOSTcmZW5jcnlwdGVkSWQ9QTA3OTYxMjkxQlRZN1A0VVNQQkkxJmVuY3J5cHRlZEFkSWQ9QTAyODAwMDYxTVk5TzVRODZRQjM3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[4:7])

    if(converted_price < 600.0):
        send_mail()

    print(title.strip())
    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('amazonpricetrack21@gmail.com', 'xsuwsncqsnvgoigp')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.ae/Apple-MWP22ZE-A-AirPods-Pro/dp/B07ZQC2G9X/ref=sr_1_1_sspa?dchild=1&keywords=apple+airpods+pro&qid=1626240693&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRTkE4NzRYTFJOSTcmZW5jcnlwdGVkSWQ9QTA3OTYxMjkxQlRZN1A0VVNQQkkxJmVuY3J5cHRlZEFkSWQ9QTAyODAwMDYxTVk5TzVRODZRQjM3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'amazonpricetrack21@gmail.com',
        'preetiwali212@gmail.com',
        msg
    )

    print('Hey, Email has been sent!')

    server.quit()


while(True):
    check_price()
    time.sleep(60*60)