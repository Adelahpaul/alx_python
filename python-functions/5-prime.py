def is_prime(number):
    if number==2 or number==3:
        return True
    if number%2==0 or number<2:
        return False
    for n in range(3,int(number**0.5)+1,2):   
        if number%n==0:
            return False   
    return True
