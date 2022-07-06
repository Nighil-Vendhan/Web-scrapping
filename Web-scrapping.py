import urllib.request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup 
wiki= "https://www.thestar.com.my/search/?q=HIV&qsort=oldest&qrec=10&qstockcode=&pgno=1"
html=urlopen(wiki)
bs= BeautifulSoup(html,'lxml')
bs
Beautiful Soup is used to extract the website page
