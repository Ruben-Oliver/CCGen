


# Valid prefixes sourced from this article: https://www.x2q.net/post/bin-iin-lookup/ - There are likely others I'm missing.
prefixes = {
    "Visa": [4],
    "Mastercard": [range(51, 56), range(2221, 2721)],
    "American Express": [34, 37],
    "Discover": [6011, range(644, 650), 65, range(622126, 622926)],
    "Diners Club International": [36, range(300, 306), 3095, 38, 39],
    "JCB": [range(3528, 3590)],
    "UnionPay": [62, 81],
    "Maestro": [50, range(56, 70), 6304, 6759, 676770, 676774],
    "RuPay": [60, 6521, 6522],
    "Mir": [range(2200, 2205)],
    "Troy": 9792
}

def luhnCheckDigit(ccnum): # This function assumes the card number passed in has already been validated to both be a valid length, and contain a valid IIN/BIN
    
    
    ccnum = str(ccnum) # Used to reverse digits for calculation, and card numbers should not be treated as one whole integer anyway
    ccnumReversed = ccnum.replace(" ", "") [::-1] # Remove spaces (if present) and reverse digits
    
    luhnSum = 0

    for digit in ccnumReversed[1::2]: # Gets every first digit from number
        luhnSum += int(digit)

    for digit in ccnumReversed[::2]: # Gets every second digit from card number
        if int(digit) * 2 <= 9:
            luhnSum += (int(digit) * 2)
        else:
            luhnSum += ((int(digit) * 2) - 9)


    nextMultiple10Found = False
    luhnSumTemp = luhnSum
    while nextMultiple10Found == False:
        luhnSumTemp += 1
        if (luhnSumTemp % 10) == 0:
            nextMultiple10Found = True
    checkDigit = luhnSumTemp - luhnSum


    return checkDigit


