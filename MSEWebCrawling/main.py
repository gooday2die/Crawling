import requests
from bs4 import BeautifulSoup
import re
import json





main_url = "http://220.149.244.192/"
result = requests.get(main_url)
result.text[:1000]
soup = BeautifulSoup(result.text, 'html.parser')


#print(soup)

def noticeKnockKnock(no): # for getting notice posts
    main_url = ("http://220.149.244.192/notice_click.php?id=" + str(no))
    result = requests.get(main_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    #print(soup)

    Title = soup.find(class_ = "post_title").get_text().replace("	","") #Title of the post
    By =  soup.find(class_ = "post_info").get_text().replace("	","") # Writer of the post, visitors , written time
    Post = soup.find(class_ = "post_detail").get_text() # details of the post
    Comments = soup.find(class_ = "reply")
    #Downloads = soup.find_all(class_ =  "post_attachment case")

    #print(Downloads)

    print("--------------------------------------------------------------------------------------------------------< Notice ID : " + str(no) +" >--------------------------------------------------------------------------------------------------------")
    print(Title)
    print("\n\n\n")
    print(By)
    print(Post)
    if (str(Comments) != "None"):
        print(Comments.get_text())
    print("\n\n\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



def normalKnockKnock(no): # for getting normal posts
    main_url = ("http://220.149.244.192/board_click.php?id=" + str(no))
    result = requests.get(main_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    #print(soup)

    Title = soup.find(class_ = "post_title").get_text().replace("	","") #Title of the post
    By =  soup.find(class_ = "post_info").get_text().replace("	","") # Writer of the post, visitors , written time
    Post = soup.find(class_ = "post_detail").get_text() # details of the post
    Comments = soup.find(class_ = "reply")

    Downloads = soup.find_all("href")

    print("---------------------------------------------------------------------------------------------------< Normal Post ID : " + str(no) +" >--------------------------------------------------------------------------------------------------------")
    print(Title)
    print("\n\n\n")
    print(By)
    print(Post)
    if (str(Comments) != "None"):
        print(Comments.get_text())
    print("\n\n\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def contactsKnockKnock():
    main_url = ("http://220.149.244.192/contact.php")
    result = requests.get(main_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    Contacts = soup.find_all ( class_ = "info")
    EmailImageURL = [img['src'] for img in soup.find_all('img')]
    #print(len(EmailImageURL))
    #print(EmailImageURL)
    print("-----------------------------------------------------------------------------------------------------< Professor's Contacts >----------------------------------------------------------------------------------------------------")
    print("")

    print("There are " + str(len(Contacts)) + " professors in MSE ]\n\n")
    MaxI = len(Contacts)

    i = 0

    while ( i < MaxI ):

        if (i == 0):
                print("< Professor # 1 >  > -------------------------------")
        if (i != 0):
                print("< Professor # " + str(i) + " > ----------------------------------")

        print(Contacts[i].get_text())
        #print(EmailImageURL[(2 + 2 * i)]) #( 2 4 6 8 )
        getEmail((EmailImageURL[(2 + 2 * i)]) , i)
        i = i + 1


    print("----------------------------------------------------------------------------------------------------------------------------------------------------")



def getEmail(URL , i):
    main_url = ("http://api.ocr.space/parse/imageurl?apikey=b2fec904f588957&url=http://220.149.244.192/" + str(URL))
    result = requests.get(main_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    JSONlist = json.loads(str(result.text))  # for JSON Query
    #print(json.dumps(JSONlist, indent=2, sort_keys=True)) #For JSON's list
    email = JSONlist['ParsedResults'][0]['ParsedText']
    print(" Email : " + str(email))







def findingNIMO():


    URL =  (soup.find_all( class_ = "single_post"))


    #print(len(URL))
    maxI = len(URL)

    #print(URL)
    URLS = [a['href'] for a in soup.find_all(class_ = "single_post")] #URLS for new posts.
    #print(URLS)

    i = 0 #all while loops
    m = 0 # just Notice while loops for saving data
    n = 0 # just Board while loops for saving data
    j = 0 # for while loop for showing data of Notice
    k = 0 # for while loop for showing data of Board



    while (i < maxI):
        if "notice_click.php" in URLS[i]:
            NoticeIDList = ""
            NoticeIDList = URLS[i].replace("notice_click.php?id=","")

            noticeKnockKnock(NoticeIDList)

            i = i + 1
            m = m + 1

        if "board_click.php" in URLS[i]:
            BoardIDList = ""
            BoardIDList = URLS[i].replace("board_click.php?id=", "").replace("&ann=" , "")

            normalKnockKnock(BoardIDList)

            i = i + 1
            n = n + 1

    print("We found those information from the index")
    print("There are " + str(m) + " recent Notice Board Posts")
    print("There are " + str(n) + " recent Normal Board Posts")




findingNIMO()





#noticeKnockKnock(1)
#normalKnockKnock(1)
#normalKnockKnock(8)

#contactsKnockKnock()

