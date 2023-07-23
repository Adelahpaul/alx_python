def validate_password(password):
    list = ['!', '@', '#', '$', '%', '&', '(', ')', '-', '_', '[', ']', '{', '}', ';', ':', '"', '.', '/', '<', '>', '?']
    estr = True
    if len(password) >= 8:
        for i in password:
            if i in list:
                estr = True
            else:
                if i.isnumeric():
                    estr = True
                else:
                    if i.isupper():
                        estr = True
                    else:
                        if i.islower():
                            estr = True
                        else:
                            return False
                        return estr
    # else:
    #     estr = False
    # return estr
