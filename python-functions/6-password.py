def validate_password(password):
    #list = ['!', '@', '#', '$', '%', '&', '(', ')', '-', '_', '[', ']', '{', '}', ';', ':', '"', '.', '/', '<', '>', '?']
    if any(i.isupper() for i in password) and any(i.islower() for i in password) and any(i.isdigit() for i in password) and len(password) >= 8:
        estr = True
    else:
        return False