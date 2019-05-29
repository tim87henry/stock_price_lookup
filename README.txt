This Python program scraps www.marketwatch.com, to find the stock price of a company, and then provides information to the user.

I have used urllib3 for http requests and BeautifulSoup for parsing the web pages.


Sample script output:

Enter the Stock symbol of the company : CSCO
Name  : Cisco Systems Inc.
Price : $53.72

-------------------------------------------------------------------------

Enter the Stock symbol of the company : CISCO

Please check the Company stock symbol

-------------------------------------------------------------------------

Enter the Stock symbol of the company : AAPL
Name  : Apple Inc.
Price : $176.15
