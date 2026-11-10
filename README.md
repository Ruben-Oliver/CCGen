
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
