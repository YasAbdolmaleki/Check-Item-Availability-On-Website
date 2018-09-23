import urllib2
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from datetime import datetime  

# Change these 2 to reuse for other websites:
# urlLink = "https://ca.louisvuitton.com/eng-ca/products/anachronism-belt-nvprod1070075v"	# testing purpose
urlLink = "https://eu.louisvuitton.com/eng-e1/products/pochette-accessoires-monogram-005656"
searchingItem = "button"
searchingAttributes = {"id": "addToCartSubmit"}
emailToNotify  = 'yasmarcu@gmail.com'

def startScrappingSchedule():
	schedule.every(1).minutes.do(scrapePage)
	while 1:
		schedule.run_pending()
		time.sleep(1)

def sendGmail():
	fromaddr = 'timetospendthemoney@gmail.com'
	msg = "\r\n".join([
	  "From: timetospendthemoney@gmail.com",
	  "To: you@gmail.com",
	  "Subject: HOLA - Your Dream Bag is Available",
	  "",
	  "TIME TO SHOPPPPP:\n" + "https://eu.louisvuitton.com/eng-e1/products/pochette-accessoires-monogram-005656"
	  ])
	username = 'timetospendthemoney@gmail.com'
	password = 'TimeToSpendMoney$$$'
	birthDay = "12/12/1992"
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, emailToNotify, msg)
	server.quit()

def scrapePage():
	print "checked time: " + str(datetime.now())
	openUrl = urllib2.urlopen(urlLink)
	parsePage = BeautifulSoup(openUrl, "html.parser")
	findAddToCartButton = parsePage.find(searchingItem, attrs=searchingAttributes) # Take out the <div> of name and get its value

	if findAddToCartButton:
		print "YAYYYYY"
		sendGmail()
	else:
		callForInquiryClass = parsePage.find("span", attrs={"class": "labelPrice callToPurchase"})
		print "BOOOOO: " + str(callForInquiryClass.text.strip())

startScrappingSchedule()
