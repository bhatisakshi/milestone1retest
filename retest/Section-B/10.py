#Question-9: Validate password using regular expression:
import re
def check_password(password):
    if 8<=len(password)<=15:
        pattern=r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!#?&]).*$'
        return bool(re.match(pattern,password))
    return False
    
password=input("Enter password: ")
print(check_password(password))