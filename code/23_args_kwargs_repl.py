>>> show_it_all(0, -1)
     a: 0
     b: -1
     c: None
  args: ()
kwargs: {}

>>> show_it_all(b=0, a=-1)
     a: -1
     b: 0
     c: None
  args: ()
kwargs: {}

>>> show_it_all(*squares)
     a: 0
     b: 1
     c: 4
  args: (9, 16, 25, 36, 49, 64, 81)
kwargs: {}

>>> show_it_all(*"First")
     a: F
     b: i
     c: r
  args: ('s', 't')
kwargs: {}

>>> show_it_all(1, 2, 3, 4, 5, d=415)
     a: 1
     b: 2
     c: 3
  args: (4, 5)
kwargs: {'d': 415}

>>> show_it_all(-5, *squares, args=415)
     a: -5
     b: 0
     c: 1
  args: (4, 9, 16, 25, 36, 49, 64, 81)
kwargs: {'args': 415}

>>> show_it_all(b="Second", **ascii)
     a: 0x61
     b: Second
     c: 0x63
  args: ()
kwargs: {'P': '0x50', 'e': '0x65', 'l': '0x6c'}
