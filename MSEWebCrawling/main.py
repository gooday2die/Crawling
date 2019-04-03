import requests
from bs4 import BeautifulSoup
import re
import json





main_url = "http://220.149.244.192/"
result = requests.get(main_url)
result.text[:1000]
soup = BeautifulSoup(result.text, 'html.parser')


#print(soup)

def noticeKnockKnock(no):
    main_url = ("http://220.149.244.192/notice_click.php?id=" + str(no))
    result = requests.get(main_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    print(soup)

    Title = soup.find(class_ = "post_title").get_text().replace("	","") #Title of the post
    By =  soup.find(class_ = "post_info").get_text().replace("	","") # Writer of the post, visitors , written time
    Post = soup.find(class_ = "post_detail").get_text() # details of the post
    Downloads = soup.find_all("href")

    print("-----------------------------------------------------------------< # " + str(no) +" Notice >-----------------------------------------------------------------")
    print(Title)
    print("\n\n\n")
    #print(By)
    print(Post)
    print("\n\n\n")



def normalKnockKnock(no):
    main_url = ("http://220.149.244.192/board_click.php?id=" + str(no))
    result = requests.get(main_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    #print(soup)

    Title = soup.find(class_ = "post_title").get_text().replace("	","") #Title of the post
    By =  soup.find(class_ = "post_info").get_text().replace("	","") # Writer of the post, visitors , written time
    Post = soup.find(class_ = "post_detail").get_text() # details of the post
    Downloads = soup.find_all("href")

    print("-----------------------------------------------------------------< # " + str(no) +" Board Issue >-----------------------------------------------------------------")
    print(Title)
    print("\n\n\n")
    #print(By)
    print(Post)
    print("\n\n\n")

def contactsKnockKnock():
    main_url = ("http://220.149.244.192/contact.php")
    result = requests.get(main_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    Contacts = soup.find_all ( class_ = "info")
    EmailImageURL = [img['src'] for img in soup.find_all('img')]
    #print(len(EmailImageURL))
    #print(EmailImageURL)

    print("There are " + str(len(Contacts)) + " professors")
    MaxI = len(Contacts)

    i = 0

    while ( i < MaxI ):
        print(Contacts[i].get_text())
        print(EmailImageURL[(2 + 2 * i)]) #( 2 4 6 8 )
        print("")
        getEmail((EmailImageURL[(2 + 2 * i)]) , i)
        i = i + 1


def getEmail(URL , i):
    main_url = ("http://api.ocr.space/parse/imageurl?apikey=b2fec904f588957&url=http://220.149.244.192/" + str(URL))
    result = requests.get(main_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    JSONlist = json.loads(str(result.text))  # for JSON Query
    #print(json.dumps(JSONlist, indent=2, sort_keys=True)) #For JSON's list
    email = JSONlist['ParsedResults'][0]['ParsedText']
    print(email)

#getEmail("http://220.149.244.192/css/image/shin_email.PNG")





def findingNIMO():
    i = 0
    SAVE = []


    URL =  (soup.find_all( class_ = "single_post"))

    print(len(URL))
    maxI = len(URL)


    while (i < maxI):
        print(URL[1])
        i = i + 1


#findingNIMO()


def traash():
    for a in soup.find_all('a', href=True):
        print("Found the URL:", a['href'])
        SAVE[i] = a['href']
        i = i + 1



#noticeKnockKnock(1)
#normalKnockKnock(2)
contactsKnockKnock()
