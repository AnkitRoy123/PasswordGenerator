import string 
import random 
while True :
  s1 = string.ascii_uppercase
  s2 = string.ascii_lowercase
  s3 = string.digits
  s4 = string.punctuation
  plen = input("Enter the length of your password:\n")
  try:
    plen = int(plen)
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print(f"Your password is: {''.join(s[0:plen])}")
  except ValueError:
    print("Enter a valid number.")
