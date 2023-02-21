def one():
    return "one"
def two():
    return "two"
def three():
    return "three"
def four():
    return "four"
def five():
    return "five"
def six():
    return "six"
def seven():
    return "seven"
def eight():
    return "eight"
def nine():
    return "nine"
def zero():
    return "zero"
def default():
    return "no spell exist"

numberSpell = {
    0: zero,
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine
    }

def spellFunction(number):
    return numberSpell.get(number, default)()
n=int(input("enter only a number"))
s=str(n)
for i in range(len(s)):
    print(spellFunction(int(s[i])),end=" ")
"""
input:
890
output:
eight nine zero
"""
