def swap(a, b):
    return b, a

def GCD(a, b=None):
    if not b:
        return a
    if b > a:
        a, b = swap(a, b)
    if a % b == 0:
        return b
    return GCD(b, a%b)

def LCM(a, b=None):
    if not b:
        return a
    return a * b * GCD(a, b)

def argsGCD(*args):
    currentGCD = None
    for arg in args:
        currentGCD = GCD(arg, currentGCD)
    return currentGCD

def argsLCM(*args):
    currentLCM = None
    for arg in args:
        currentLCM = LCM(arg, currentLCM)
    return currentLCM