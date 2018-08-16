#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib2

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def extract_server(s):
  while True:
    underpos = s.find('_')
    if underpos == -1:
      break
    elif underpos == len(s)-1:
      return s[:-1]
    s=s[underpos+1:]
  return 'http://'+s

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  server = extract_server(filename)
  # print server
  url_list = []
  with open(filename,'rU') as f:
    regex = re.compile(r'GET\s+(.*puzzle.*)\s+HTTP')
    for line in f:
      match = re.search(regex,line)
      if match:
        possible_url = server + match.group(1)
        if possible_url not in url_list:
          url_list.append(possible_url)
        # print match.group(1)
  f.closed

  place_case = True
  regex_place = re.compile(r'-\w+-(\w+)\.jpg$')
  for url in url_list:
    if not re.search(regex_place,url):
      place_case = False
      break
  if place_case:
    return sorted(url_list,key = sorter_for_place_finder )
  return sorted(url_list)

def sorter_for_place_finder(s):
  s=s[:-4]
  while True:
    dashpos = s.find('-')
    if dashpos!=-1:
      s=s[dashpos+1:]
    else:
      return s 

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir,0755)
  
  if os.path.isfile(dest_dir):
    print "Destination should be a directory, not a file!"
    sys.exit(1)
  filelist=[] # lista care se genereaza pe masura ce se creeaza fisierele
  for i,url in enumerate(img_urls):
    req = urllib2.Request(url)
    try:
      print 'Retrieving...',
      response = urllib2.urlopen(req)
    except urllib2.URLError as e:
      if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
      elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
    else:
    # everything is fine
      print 'Done'
      file_to_be_created = 'img' + str(i)
      with open(os.path.join(dest_dir,file_to_be_created),'w') as f:
        f.write(response.read())
      f.closed
      filelist.append(file_to_be_created)
  # gata aici am terminat cu downloadul si am scris si fisierele
  generate_index(dest_dir,filelist)
  
def generate_index(dest_dir,filelist):
  images = sorted(filelist,key = lambda x: int(x[3:]) )
  html_images_reference =''
  for image in images:
    html_images_reference+='<img src="{0}">'.format(image)
  indexhtml = '''<verbatim>
<html>
<body>'''+html_images_reference+'''</body>
</html>
'''
  with open(os.path.join(dest_dir,'index.html'),'w') as f:
    f.write(indexhtml)
  f.closed

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  #sys.exit(1)
  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
  #generate_index('animaldir',os.listdir('animaldir'))
