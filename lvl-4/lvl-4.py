import urllib2

def getPage(endString):
	#This function takes the standard ?nothing= URL suffix and adds on endString
	#Found by autoloading and searching each page for a numeric value
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(endString)
	print url
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return response.read()
	

newPage = getPage("12345")
nextPage = ""
x = 0
while x <= 400:
	
	for item in newPage:
		if not item.isdigit():
			nextPage = ""
		elif item.isdigit():
			nextPage += item
	print nextPage
	newPage = getPage(nextPage)
	x += 1
	print "iteration \#" + str(x)