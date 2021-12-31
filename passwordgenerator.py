import random

kleineletters = "abcdefghijklmnopqrstuvwxyz"
hoofdletters = "ÄBCDEFGHIJKLMNOPQRSTUVWXYZ"
getallen = "0123456789"
symbolen = "[]{}();*/-_!?#%+="

alles = kleineletters + hoofdletters + getallen + symbolen

lengte = 16

password = "".join(random.sample(alles, lengte))

print(password)
