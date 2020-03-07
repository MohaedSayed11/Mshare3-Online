factors = []
def getFactors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

print(getFactors(50))
primefactors = []

for j in factors:
    if j % 2 != 0:
        primefactors.append(j)

def largestprimefactor():
    pass
print(primefactors)
