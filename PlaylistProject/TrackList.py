import requests
from bs4 import BeautifulSoup
import re
import json
import MysqlQuery



#For Tracklist Crawling Functions Start


import mysql.connector



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
        CurrentTrack = JSONlist['tracks'][i]['trackTitle']
        print(CurrentTrack)
        MysqlQuery.inputToDB(CurrentTrack,URL)
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

def GetTrackListCommand():
    print("Query for :")
    search = input("")
    GetTracklist(search)

    print("")
    print("Tracklist For :")
    URL = input("")
    GetTracks(URL)

    return

GetTrackListCommand()
#GetTracks("https://www.1001tracklists.com/tracklist/2bq6fvfk/illenium-live-arena-ultra-music-festival-miami-miami-music-week-united-states-2019-03-30.html") For Example