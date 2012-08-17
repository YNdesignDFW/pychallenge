import urllib2

def getPage(bs):
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(bs)
	print url
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return response.read()
	
print getPage("12345")