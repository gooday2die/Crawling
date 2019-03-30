import requests
from bs4 import BeautifulSoup


main_url = "http://books.toscrape.com/index.html"
result = requests.get(main_url)

result.text[:1000]
soup = BeautifulSoup(result.text, 'html.parser')

#print(soup.prettify()[:1000])



def getBookInfo():
    main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]
    print(str(len(main_page_products_urls)) + " fetched products URLs")
    print("One example:")

    i = 0
    while (i < 20):
        print(main_page_products_urls[i])
        i = i + 1




getBookInfo()