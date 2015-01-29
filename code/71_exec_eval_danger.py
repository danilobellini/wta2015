# NÃO RODE ISTO! Equivale a rm -rf /
"""
import os
for root, dirs, files in os.walk("/"):
  for fname in files:
    try:
      os.remove(os.path.join(root, fname))
    except:
      pass
"""