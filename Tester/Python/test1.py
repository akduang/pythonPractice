import copy
a = ('a','b','c')
c = copy.copy(a)
d = copy.deepcopy(a)
if c == d:
  print("c和d的值相等")
if id(c) == id(d):
  print("c和d的地址相等")