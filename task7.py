import re

emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", "nasa@sa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@extra123.123", "fake@fake123.fakercom"]

pattern = re.compile(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$')

# valid = [email for email in emails if pattern.match(email)]
# print(valid)

def isValid(emails):
    valid_email = []  
    for e in emails:
        if re.match(pattern, e):  
            valid_email.append(e)  
    return valid_email

print(isValid(emails))
