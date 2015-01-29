#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Thu Sep 25 17:50:04 2014
# @author: Danilo de Jesus da Silva Bellini

if "__path__" in locals():
  print("Imported package {}\n  from this path: {}\n  filename: {}"
        .format(__name__, __path__[0], __file__))
else:
  print("Imported module {}\n  filename: {}".format(__name__, __file__))
