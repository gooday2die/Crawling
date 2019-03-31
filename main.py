import requests
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import re


main_url = "http://books.toscrape.com/index.html"
result = requests.get(main_url)
result.text[:1000]
soup = BeautifulSoup(result.text, 'html.parser')

#print(soup.prettify()[:1000])



no = 1

def getBookInfo():
    main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]
    print(str(len(main_page_products_urls)) + " fetched products URLs")

    i = 0
    while (i < 20):
        print(main_page_products_urls[i])
        i = i + 1
# just for testing modules.
# ignore this function.

#getBookInfo()




def getBookName(): #Get all Book names from the page.
    main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]

    i = 0 # For while loop
    print("There are " + str(len(main_page_products_urls)) +" Books in the page")
    while (i < len(main_page_products_urls)):
        request_url = "http://books.toscrape.com/"+str(main_page_products_urls[i])
        #print(request_url)
        result2 = requests.get(request_url)
        result2.text[:1000]
        soup2 = BeautifulSoup(result2.text, 'html.parser')
        title = soup2.find("h1") #variable title is the one with html tags
        #print(soup2)
        BookName = title.get_text() #variable BookName is the on without html tags. Just book names.
        print("# " + str(i+1) +" " +str(BookName))
        i = i + 1

#getBookName()


def getBookPrice(): #Get all the Book price from the page
    main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]

    i = 0 # For while loop
    print("There are " + str(len(main_page_products_urls)) +" Books in the page")
    while (i < len(main_page_products_urls)):
        request_url = "http://books.toscrape.com/"+str(main_page_products_urls[i])
        #print(request_url)
        result3 = requests.get(request_url)
        result3.text[:1000]
        soup3 = BeautifulSoup(result3.text, 'html.parser')
        price = soup3.find_all("td")
        BookPrice = price[2]
        BookPrice.get_text()
        print(BookPrice.get_text())


        i = i + 1




def getSpecificBookName(no):
    request_url = "http://books.toscrape.com/"+str(main_page_products_urls[no])
    #print(request_url)
    result = requests.get(request_url)
    result.text[:1000]
    soup = BeautifulSoup(result.text, 'html.parser')
    title = soup.find("h1") #variable title is the one with html tags
    #print(soup2)
    BookName = title.get_text() #variable BookName is the on without html tags. Just book names.
    print("# " + str(no+1) +" " +str(BookName))



def getSpecificBookPrice(no):
    request_url = "http://books.toscrape.com/"+str(main_page_products_urls[no])
    #print(request_url) #check url we are on
    result = requests.get(request_url)
    result.text[:1000]
    soup = BeautifulSoup(result.text, 'html.parser')
    tdValue = soup.find_all("td") #tdValue is the all the data from the query td, 0:id , 1: cat, 2: price ex tax, 3: price with tax, 4: tax, 5:isAvail, 6: no of Reviews
    tdPrice = tdValue[2]
    BookPrice = (tdPrice.get_text()).replace("Â", "")
    print("    Price : " + BookPrice)

def getSpecificBookAvail(no):
    request_url = "http://books.toscrape.com/"+str(main_page_products_urls[no])
    #print(request_url) #check url we are on
    result = requests.get(request_url)
    result.text[:1000]
    soup = BeautifulSoup(result.text, 'html.parser')
    tdValue = soup.find_all("td") #tdValue is the all the data from the query td, 0:id , 1: cat, 2: price ex tax, 3: price with tax, 4: tax, 5:isAvail, 6: no of Reviews
    #print(tdValue) #print for visuals
    Availability = tdValue[5]
    Availability.get_text()
    print("    Availability : " + str(Availability.get_text()))

def getSpecificBookRating(no):
    request_url = "http://books.toscrape.com/"+str(main_page_products_urls[no])
    #print(request_url) #check url we are on
    result = requests.get(request_url)
    result.text[:1000]
    soup = BeautifulSoup(result.text, 'html.parser')
    pValue = soup.find_all("p")
    Ratings = soup.find("p", class_ = re.compile("star-rating")).get("class")[1]
    #print(pValue[2])
    print("    The rating of the book is " + str(Ratings))


def getSpecificBookImg(no):
    request_url = "http://books.toscrape.com/"+str(main_page_products_urls[no])
    #print(request_url) #check url we are on
    result = requests.get(request_url)
    result.text[:1000]
    soup = BeautifulSoup(result.text, 'html.parser')
    imgValue = soup.find("img").get("src") #image url with html tags. ../../blah/blah
    imgURL = "http://books.toscrape.com/" + imgValue.replace("../", "") #clean up just the url
    print("    Image URL : " + imgURL)




#Function Starts from Here.

main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]
print("There are " + str(len(main_page_products_urls)) +" Books in the page")

totalBookNO = len(main_page_products_urls)

i = 0 #i is for while loop
while (i < totalBookNO):
    getSpecificBookName(i)
    getSpecificBookPrice(i)
    getSpecificBookAvail(i)
    getSpecificBookRating(i)
    getSpecificBookImg(i)
    print("")

    i = i + 1

