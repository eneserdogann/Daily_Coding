n = 4

def canWinNim(n):
    return False if n % 4 == 0 else True

print(canWinNim(n))