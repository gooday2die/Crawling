import beatport

a = beatport.Artists(id=69549)
print (a.data[0]['name'])
print (a.tracks[1]['title'])


