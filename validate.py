import pandas as pd

# Validate Luhn Check Digit
def validateCheckDigit(digits):
    digitsToCheck = str(digits) # Used to reverse digits for calculation, and card numbers should not be treated as one whole integer anyway
    digitsReversed = digitsToCheck.replace(" ", "")[:-1] [::-1] # Remove spaces (if present) and reverse digits
    
    print(f"Reversed Digits: {digitsReversed}")
    luhnSum = 0

    for digit in digitsReversed[1::2]: # Gets every first digit from number
        luhnSum += int(digit)

    for digit in digitsReversed[::2]: # Gets every second digit from card number
        if int(digit) * 2 <= 9:
            luhnSum += (int(digit) * 2)
        else:
            luhnSum += ((int(digit) * 2) - 9)


    nextMultiple10Found = False

    if (luhnSum % 10) == 0:
        checkDigit = 0
        nextMultiple10Found = True
    

    luhnSumTemp = luhnSum
    while nextMultiple10Found == False:
        luhnSumTemp += 1
        if (luhnSumTemp % 10) == 0:
            nextMultiple10Found = True
    checkDigit = luhnSumTemp - luhnSum

    if str(checkDigit) == str(digitsToCheck)[-1]:
        return True
    else:
        return False

# Unsure what further validation functions to add. Originally I considered
# checking numbers against my dict of valid networks/issuers, but I'm 100% certain
# that I'm missing some niche/regional prefixes/lengths anyway, and real localisation
# sounds like a nightmare.

def lookupBin(prefix):
    bins = pd.read_csv("bins.csv", dtype={"bin": "string"})

    results = bins[bins['bin'].str.startswith(prefix)].values.tolist()


    return results
    
    
