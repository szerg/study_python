#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  base = os.path.abspath(dir)
  file_list = os.listdir(dir)
  special_file_list = []
  for filename in file_list:
    match = re.search(r'__\w+__', filename)
    if match:
      special_file_list.append(os.path.join(base,filename))
  return special_file_list

def copy_to(paths,dir):
  full_path = os.path.abspath(dir)
  if os.path.exists(full_path):
    if os.path.isfile(full_path):
      print "Destination is a file. Please specify a dir."
      sys.exit(1)
  else:
    os.mkdir(full_path,0755)
  for filepath in paths:
    shutil.copy(filepath,full_path)

def zip_to(paths,zippath):
  import subprocess
  # print 'I\'m gonna run {0} {1} {2} {3}'.format('tar','-czvf',zippath,' '.join(paths))
  command = 'tar -czvf '+zippath+' '+' '.join(paths)
  print command
  subprocess.call(command,shell=True)
  # try:
  #   subprocess.check_call(["tar","-czvf",zippath,' '.join(paths)])
  # except subprocess.CalledProcessError as e:
  #   print e.returncode


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    try:
      todir = args[1]
      files_to_copy = get_special_paths(args[2])
    except IndexError as e:
      print "Incorrect number of args."
      sys.exit(1)
    del args[0:2]
    copy_to(files_to_copy,todir)
    sys.exit(0)

  tozip = ''
  if args[0] == '--tozip':
    try:
      tozip = args[1]
      files_to_zip = get_special_paths(args[2])
    except IndexError as e:
      print "Incorrect number of args."
      sys.exit(1)
    del args[0:2]
    zip_to(files_to_zip,tozip)
    sys.exit(0)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # so now I'm in the case where I have at least one arg but no option set so to speak
  # check for duplicate folders
  if len(set(args)) != len(args):
    print "Bah! Tu ma faci sa printez de 2 ori?!"
    sys.exit(1)

  for folder in args:
    for special_path in get_special_paths(folder):
      print special_path
    

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
