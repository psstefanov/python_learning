import urllib
import re

symbollist = ["appl", "spy", "goog", "nflx"]
i=0

while i < len(symbollist):
    url = "https://beta.finance.yahoo.com/quote/" +symbollist[i]
    print url
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    #print htmltext
    #regex = 'span if="yfs_184_'+symbollist[i] +'">(.+?)</span>'
    regex = '<span class="D(ib) Fz(24px) Fw(b) Trsdu(0.3s)" data-test="qsp-price" data-reactid=".1ralcrm9n9c.1.2.$main-0-quote.1.0.0.0.2:$price.0">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    #print "The price of", symbollist[i], " is ", price

    i+=1