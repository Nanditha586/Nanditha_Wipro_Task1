import re
def validate_password(password):
    pattern = r'''
    ^
    (?=.*[A-Z])
    (?=.*[a-z])
    (?=.*\d)
    (?=.*[!@#$%^&*_+\-])
    [A-Za-z0-9!@#$%^&*_+\-]{8,}
    $
    '''

    if re.match(pattern, password, re.VERBOSE):
        print("Strong Password")
    else:
        print("Weak Password")
pwd = input("Enter your password: ")
validate_password(pwd)