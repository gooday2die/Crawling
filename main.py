import requests
from bs4 import BeautifulSoup
import re
import json

main_url = "http://books.toscrape.com/index.html"
result = requests.get(main_url)
result.text[:1000]
soup = BeautifulSoup(result.text, 'html.parser')

#print(soup.prettify()[:1000])

#For Book Crawling Functions Start


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
    print("# " + str(no) +" " +str(BookName))



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
#Right Below is Global Declaration
#getCommand Function is a recursive function.

main_page_products_urls = [x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")]
totalBookNO = len(main_page_products_urls)
#print("There are " + str(len(main_page_products_urls)) +" Books in the page")

command = 0

def getCommand():
    print("")
    print("Maunal Search : M")
    print("Automatic Search : A")
    print("Quit : Q")
    print("")
    command = input()

    if (command == "M" or command == "m"):
        print("Enter Book Number (Starts from 0)")
        manual = int(input())
        bookno = manual

        getSpecificBookName(bookno)
        getSpecificBookPrice(bookno)
        getSpecificBookAvail(bookno)
        getSpecificBookRating(bookno)
        getSpecificBookImg(bookno)

        getCommand()

    if (command == "A" or command == "a"):
        i = 0 #i is for while loop
        while (i < totalBookNO):
            print("")
            getSpecificBookName(i)
            getSpecificBookPrice(i)
            getSpecificBookAvail(i)
            getSpecificBookRating(i)
            getSpecificBookImg(i)
            print("")
            i = i + 1

        getCommand()

    if (command == "Q" or command == "q"):
        exit()


    if (command != "A" and command != "M" and command != "Q" and command != "a" and command != "m" and command != "q"):
        print("Wrong Value")
        print("")
        getCommand()
#For Book Crawling Functions Ended

#getCommand()



#For Tracklist Crawling Functions Start

def GetTracks(URL):
    print("")
    main_url="https://1001tracklist-api.azurewebsites.net/api/tracklist/tracks?tracklistURL="+str(URL)
    result = requests.get(main_url)
    JSONlist = json.loads(str(result.text)) #for JSON Query
    #print(json.dumps(JSONlist, indent=2, sort_keys=True)) #For JSON's list

    maxlength =  (len(JSONlist["tracks"])) #maxlength is for lines of JSON files

    i = 0
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("There are " + str(maxlength) + " tracks in this set")
    print("")



    while(i< maxlength):
        print("")
        print("# " + str(i + 1) + " Track")
        print(JSONlist['tracks'][i]['trackTitle'])
        print("")

        i = i + 1

    #newresult = json.loads(str(result))

    #Tracklists = (((((result.text.replace("},{", "\n")).replace("\"trackTitle\":","").replace("{\"tracks\":[{",""))).replace(",\"timestamp\":*","").replace("}]}","")))
    #print(Tracklists)


def GetTracklist(search):
    print("")
    main_url="https://1001tracklist-api.azurewebsites.net/api/tracklists?query=" + str(search)
    result = requests.get(main_url)

    JSONlist = json.loads(str(result.text)) #for JSON Query
    #print(JSONlist) #for Printout
    #print(json.dumps(JSONlist, indent=2, sort_keys=True)) #For JSON's list

    #JSON

    maxlength =  (len(JSONlist["results"])) #maxlength is for lines of JSON files
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    print("We found " + str(maxlength)+ " recent tracklists")
    print("")

    i = 0
    while ( i < maxlength ):
        print("")
        print (JSONlist['results'][i]['link'])
        print (JSONlist['results'][i]['title'])
        print ("")

        i = i + 1

    #link = JSONlist['results'][0]['link']
    #title = JSONlist['results'][0]['title']

    #print(title)
    #print(link)

    #SearchLists = (((result.text.replace("},{","\n")).replace("{\"results\":[{","")).replace("}]}","")).replace("\"title\":","")
    #print(SearchLists)

def gettracklistcommand():
    print("Query for :")
    search = input("")
    GetTracklist(search)

    print("")
    print("Tracklist For :")
    URL = input("")
    GetTracks(URL)

gettracklistcommand()
