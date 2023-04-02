# Created By MOP ( Mother Of Programmers )
import random
import os
import string
import time
import secrets

# Below Code Is Cryptograpically Encrypted Code
# You can change the character size by changing the size of range below the random_code variable

print("""
=================================
= COMBINED RANDOM KEY GENERATOR =
=================================
Note: You Will See The Combined Code On A Text File The Other Codes Will Appear On The Terminal Or CMD
""")

random_code = (''.join(secrets.choice(string.ascii_lowercase + string.ascii_uppercase) for i in range(7)))
print(f"The Random Code: {random_code}")

# Below Here We Make A Random Text But Not Encrypted Via Cryptography

random_text = (''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=10)))
print(f"The Random Text: {random_text}")

# Loops Are Not Working On This Code
# Same Character Will Print On The Screen When You Use A Loop
# Below Here We Make A Very Good Combination With The random_code and random_text variables

random_all =  (random_code + random_text)
#print(f"The Combined Code: {random_all}")

# When We Make It Like This Method The Decryptors Can't Decrypt As Might As Well
# And So Below Codes Do Make Save The Combined Codes To A Text File
# You Just Need To Execute This File Some Times More To Generate Some Combined Codes And They Will Save On The Text File Called As "randomcodes.txt"
# When You Open The .txt File You Will Able To See The All The Codes On The File

file_name = "randomcodes.txt"
file = open(file_name, 'a')
line = random_all + '\n'
file.write(line)
print(f"Codes Are Saved On '{file_name}'")

