from bs4 import BeautifulSoup
import csv
import requests
import time
with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "price", "availability", "rating"])

    for page in range(1, 51):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        books = soup.find_all("article", class_="product_pod")
    
    
        for book in books:

            title = book.find('img')['alt']
            price1 = book.find("p", class_="price_color").text.replace('Â', '')
            price = float(price1.replace('£', ''))
            availability = book.find('p', class_ = 'instock availability').text.strip()
            rating = book.find('p')["class"][1]
            writer.writerow([title, price, availability, rating])
        time.sleep(2)
        
        