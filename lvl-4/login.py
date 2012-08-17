import urllib
import urllib2
import cookielib
 
def login():
    url = "http://domain.com/login.php "  # example url
 
    opts = {
    'user': 'yourUSERNAME',
    'password': 'yourPASS',
    'server': 'serverName'
    }
 
    data = urllib.urlencode(opts)
 
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12',
    'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
    'Accept-Language': 'en-gb,en;q=0.5',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Connection': 'keep-alive'
    }
 
    req = urllib2.Request(url, data, headers)
 
    response = ClientCookie.urlopen(req)
    return response.read()