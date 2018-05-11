class A():
  pass

class B(A):
  pass

print(dir(__doc__))

print(B().__doc__)