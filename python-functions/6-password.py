def validate_password(password):
    xtrs = "abcde"
    nbrs = "1234"
    if password >=8 and password >=xtrs.upper and password >=xtrs.lower and password >=nbrs:
        return True
    else:
        return False