import re
a = input("Password: ")
b = True

while a:
    if (len(a)<6 or len(a)>16):
        break
    elif not re.search("[a-z]",a):
        break
    elif not re.search("[A-Z]",a):
        break
    elif not re.search("[0-9]",a):
        break
    elif not re.search("[$#@]",a):
        break
    else:
        print("Access granted!")
        b = False
        break

if b:
    print("Access denied!")