#Password validator is a program that validates password to match specific
# rules. For example, the minimum lenght of the password must be eight
# charakters long and it should have at least one uppercase letter in it.
#
# A valid password is one that conforms to the following rules :
# -Minimum lenght is 5;
# -Maximum lenght is 10; Should cotain at least one number;
# -Should contain at least one special character (such as !,@,#,$,%,^,&,*)
# -Should not contain spaces.

import re
password = input("Enter your password :")
flag = 0

while True :
    if len(password) < 5:
        flag = -1
        break
    elif len(password) > 10:
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]",password):
        flag = -1
        break
    elif re.search(" ", password):
        flag = -1
        break
    elif not re.search("['!','@','#','$','^','&','*','-','_','+','=','\',';',':','<','>','.','?']", password):
        flag = -1
        break
    else:
        flag = 0
        print("Password is valid!")
        break

if flag == -1:
    print("Not a valid password!")
