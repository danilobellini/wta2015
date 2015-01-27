#!/bin/sh
# Created on 2015-01-26 月 22:15:30 BRST
# By Danilo J. S. Bellini
mkdir -p rtf
ls *.py | while read fullname ; do
  name=${fullname%.py}
  pygmentize -O full,style=monokai -o rtf/$name.rtf $fullname
done

