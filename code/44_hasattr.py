import itertools
if hasattr(itertools, "accumulate"):
    print("Python 3") # A rigor, 3.2+
else:
    print("Python 2") # Talvez 3.0 / 3.1
