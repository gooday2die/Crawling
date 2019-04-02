import mysql.connector



def inputToDB(Trackname , From):
    cnx = mysql.connector.connect(user='gooday2die', password='gooday2die',
                              host='db4free.net',
                              database='playlist')


    cursor = cnx.cursor()

    add_employee = ("INSERT INTO `Test02` (`TrackName`, `From`) VALUES ('"+str(Trackname)+"', '"+str(From)+"')")



    cursor.execute(add_employee)


    cnx.commit()

    cursor.close()
    cnx.close()

    print("Sent "+str(From) + " And "+ str(Trackname) +" To the DB")

