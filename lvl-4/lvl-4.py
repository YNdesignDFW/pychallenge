import urllib2

def getPage(endString):
	#url holds the attached string of the baseline URL that does not change 
	#and endString, the string that is located by another function and passed to 
	#this one as a parameter
	url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(endString)
	#uncomment "print url" below as needed for debugging purposes
	#print url 
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	return response.read()
	

newPage = getPage("43650")
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