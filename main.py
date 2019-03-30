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

    i = 0
    while (i < 20):
        print(main_page_products_urls[i])
        i = i + 1



#getBookInfo()




def getBookName():
    main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]

    i = 0
    print(len(main_page_products_urls))
    while (i < len(main_page_products_urls)):
        request_url = "http://books.toscrape.com/"+str(main_page_products_urls[i])
        #print(request_url)
        result2 = requests.get(request_url)
        result2.text[:1000]
        soup2 = BeautifulSoup(result2.text, 'html.parser')
        title = soup2.find("h1")
        #print(soup2)
        BookName = title.get_text()
        print("# " + str(i+1) +" " +str(BookName))
        i = i + 1

getBookName()
