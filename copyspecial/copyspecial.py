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
    filenames = os.listdir(dir)    
    abspath = os.path.abspath(dir)
    
    paths = []
    for filename in filenames:
      if not os.path.isdir(filename):
        paths.append(os.path.join(abspath, filename))
    
    return paths

def copy_to(paths, dir):
    if not os.path.exists(dir):
      os.mkdir(dir)
    
    abspath = os.path.abspath(dir)
    
    for path in paths:
      basename = os.path.basename(path)
      shutil.copy(path, os.path.join(abspath, basename))
      print "Copying..."
      print path
      print "to..."
      print os.path.join(abspath, basename)
      
    return

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
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  files = get_special_paths(args[0])
  
  if todir:
    copy_to(files, todir)
  elif tozip:
    sys.exit(1)
  else:    
    print "\n".join(files) + "\n"
  
if __name__ == "__main__":
  main()
