#!/bin/sh
# by Danilo J. S. Bellini
# A simple script to add all files in this directory using their modification
# timestamp as their commit date, with a commit per file
ls *.* -rt | while read f ; do
  git add "$f"
  git commit -m"Add $f" --date="$(stat "$f" -c %y)"
done

