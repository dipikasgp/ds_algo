
def checkArmstrong(n):
    x = n
    final_num = 0
    num_len = len(str(n))
    while n>0:
        rem = n%10
        final_num+= rem ** num_len
        n = n//10
    if final_num == x:
        return True
    else:
        return False

