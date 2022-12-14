import random


def ValidateNumber(userInput):
    print(userInput)
    try:
        inputNumber = int(userInput)
    except ValueError:
        return "Not an integer"
    else:
        if inputNumber < 2:
            return "Number cannot be lower than 2"
        return IsPrime(inputNumber)


def IsPrime(n):
    if n != int(n):
        return False
    n = int(n)
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def TrialComposite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(15):  # number of trials
        a = random.randrange(2, n)
        if TrialComposite(a):
            return False

    return True
