def nearest_sq(n):
  a =  (int(n**0.5)+1)**2
  b =   int(n**0.5)**2
  if (n - b) < (a - n):
    return b
  else :
    return a