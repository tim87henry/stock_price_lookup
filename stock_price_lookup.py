from bs4 import BeautifulSoup
import urllib3
import re

try:
    # Disable urllib3 InsecureRequestWarning message
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http=urllib3.PoolManager()
	
	#Obtain the Stock symbol from the user and open the required page from marketwatch.com
    cmp=input("Enter the Stock symbol of the company : ")
    page_data=http.request('GET',"https://www.marketwatch.com/investing/stock/"+cmp)
	
	# Parse the web page using BeautifulSoup
    page_content=BeautifulSoup(page_data.data,"html.parser")
	
	# Use regexp to obtain the company name and stock price from the page contents
    price=re.search(r"(\s)*Delayed quote[\n]*[$]\n([\d,]+\.\d+)",page_content.text)
    name=re.search(r"[|] (.*) Stock Quote",str(page_content.title))
	
	#Display the obtained information
    print("Name  : "+str(name.group(1)))
    print("Price : $"+str(price.group(2)))
	
except:
    # Catch exception in case the stock symbol is wrong
    print("\nPlease check the Company stock symbol")

