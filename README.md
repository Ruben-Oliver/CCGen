
# CCGen (working title)

This tool generates mathematically valid credit/debit card numbers that conform to ISO/IEC 7812 standards, as well as selecting from (major) card networks.

It can also validate the last digit of a given card to see if it passes the Luhn algorithm check.
Currently, the validator is unable to determine a cards validity based on it's BIN/IIN. I may add this feature in the future, but it would require a separate database with massive amounts of information on every possible known identifier.


The generator follows these rules:
- Possible lengths between 12 and 19, depending on the network
- Valid prefix depending on card network
- Valid check digit following the Luhn algorithm

I mostly made this to keep my Python skills sharp and to learn about credit/debit card standards, but if you find a real use for it 
then that's great!


## `generate.py` Functions

1. `checkLength(network, length)`  
This function is used to check that specified desired length of the card number is in line with the major network's outlined lengths. E.g, Mastercard supports a length of 16, which will pass this check. It does *not* support a length of 19 (like Discover, for example), and so this length will fail the check

    This function will return a boolean `True` or `False`.

2. `checkPrefix(network, prefix)`
This function is used to check that specified desired prefix of the card number is in line with the major network's outlined prefixes. E.g, Mastercard supports a prefix of 51, which will pass this check. It does *not* support a prefix of 6521  (like RuPay, for example), and so this prefix will fail the check 

    This function will return a boolean `True` or `False`.

3. `generatePAN(network, length, prefix)`
This function takes the desired card network, card number length, and its' prefix and randomly generates the remaining digits. It generates the number of digits required to reach the desired length *after* the length of the prefix but *before* reaching the final digit, because the final digit is reserved for the Luhn check digit. For example, a prefix of 4 digits with a desired card number length of 16 will yield a total of 11 digits from this function  
  
    *Technically*, not all the digits it generates will actually be part of the PAN (primary account number), as the first few after the prefix are generally used to identify the issuer/bank. Because this is a quick and dirty project, I do not think I'll be adding valid issuer identifiers for every possible bank and card issuer on Earth.

    This function will return a card number (*including* prefix) missing the final digit.

4. `luhnCheckDigit(digits)`  
This function will take a card number (except for the final digit), and work out what the final digit should be according to the Luhn (also known as Mod 10) algorithm.  

    This function will return a single digit as a string to be appended as the final digit in the card number.

5. `pickRandom(randomType, network)`  
This function can pick random values for the network, the possible length, as well as the card numbers' prefix. If you need a random length or prefix, then you *must* pass in a valid network. This function really sucks in its' current state and I might improve it later, but it technically works for the purpose of the final function below.

    This function will return a randomly picked network as a string, a length as an integer, and a prefix as a string.

6. `generateCard(network, length, prefix)`  
This function combines all the above functions in tandem to generate a full mathematically valid card number. While it can take arguments for the network, length and prefix, none of them are strictly required and you may leave the function call empty. In this case, it will pick three random (but valid) values for each parameter anyway.  

    This function will return a full valid card number as a string.
  


## `validate.py` Functions

1. `validateCheckDigit(digits)`  
This function validates whether or not a card numbers' check digit matches with what the Luhn Algorithm dictates.

    This function will return a boolean `True` or `False`.

2. `lookupBin(prefix)`
This function takes a card number prefix and uses Pandas to open a local `bins.csv` file containing a maintained list of known BIN/IIN prefixes. Credit for this list goes to Techbuddie-Solutions and their [binlist-data repository](https://github.com/Techbuddie-Solutions/binlist-data).

    This function will return a list of results, each result is itself a list containing data in the below format:
    `[bin, brand, type, category, issuer, issuer_phone, issuer_url, alpha_2, alpha_3, country, source, seen]`

    There will be one of these lists for every returned result for the given prefix.




# Credits

`bins.csv` (list of known BIN/IIN numbers) was sourced from [Techbuddie-Solutions](https://github.com/Techbuddie-Solutions/binlist-data), maintainer of [binlist.io](https://binlist.io). Thanks!