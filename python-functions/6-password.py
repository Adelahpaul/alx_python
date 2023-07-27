 #!/usr/bin/env python3
def validate_password(password):
    if len(password) >= 8 and any(i.isupper() for i in password) and  any(i.islower() for i in password) and any(i.isdigit() for i in password):
        return True
    elif (i.isspace() for i in password):
        return False
    else:
        return False