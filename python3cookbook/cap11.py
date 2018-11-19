# network si web programming
# foloseste http://httpbin.org ca sa iti testezi client code-ul

# e utila daca vrei sa faci simple GETs sau POSTs , altfel e mai greu de  utilizat
# foloseste-o intr-un context corect, cu exceptii
import urllib.request
import urllib.error
import urllib.parse

import pprint

url = 'http://httpbin.org/post'

# pt a adauga parametri treb sa faci un dictionar si apoi sa encodezi dictionarul ca sa il dai requestului
params = {'a':1,'b':2}
querystring = urllib.parse.urlencode(params)

# GET cu params chiar in url
#req = urllib.request.Request(url+'?'+querystring)
# POST
req = urllib.request.Request(url,querystring.encode())


try:
    # pt un req asa simplu merge pus direct url-ul
    resp = urllib.request.urlopen(req)
except urllib.error.URLError as url_err:
    if hasattr(url_err, 'reason'):
        print('We failed to reach a server. Poate sunt probl de  conectivitate sau adresa nu e corecta, site-ul e jos etc')
        print('Reason: ', url_err.reason)
    elif hasattr(url_err, 'code'):
        print('The server couldn\'t fulfill the request. Nu primesti un cod 2xx , primesti not found,forbidden etc')
        print('Error code: ', url_err.code)
else:
    pprint.pprint(resp.read())