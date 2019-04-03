MSE Homepage Crawling Bot
For Learning Python. Making a Crawling Bot for our MSE Homepage.

Get Basic Board Informations
(such as Notice Board , Free Board) 

- Notice ...  Done!
  Need attachments part. (Seems Easy)
  
- All Boards ...  Done!
  Need attachments part. (Seems Easy)

- Professor Contacts ... Done!
  Since the emails of professors are saved as an image file, I used OCR to get professor's emails.
  api.ocr.space -> Free , but kind of slow for now.
  (I am trying to use pytesseract which uses google's Tesseract OCR engine. But I don't know how to get it)
  
  It returns JSON file as it's result. 



TODO List

We can see that all the posts have specific nubmer. 
For Example, notice_click.php?id=1

But this bot does not know where to stop.
It can go up to notice_click.php?id=100000000 which does not exist.

So we need to limit the max nubmer.


    We can solve this problem by using the index.html.
    The latest ones are on the index main page. So by using that, We can see the limit of the pages.
