import random
import string
password=""

for i in range(0,13):
    rand=random.randint(1,3)
    if(rand==1):
        random_number = random.choice(string.digits)
        password=password +random_number
    elif(rand==2):
        random_letter = random.choice(string.ascii_letters)
        password=password +random_letter
    else:
        random_special = random.choice(string.punctuation)
        password=password +random_special
        
        
print("Your Random Password is:",password)
        
    