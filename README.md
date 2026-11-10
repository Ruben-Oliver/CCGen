
# CCGen (working title)

This tool will generate mathematically valid credit/debit card numbers that conform to ISO/IEC 7812 standards.

- Possible lengths between 12 and 19 depending on card network
- Various prefixes depending on card network
- Valid check digit following the Luhn algorithm

The goal is to create a tool that can generate theoretically valid card numbers that will pass validation checks, but not necessarily work as real chargeable cards.
The intended use is *not* to come up with real card numbers.

*Note: May make this tool validate as well as generate*