import random
# The program will take the generation in steps, first determining a length for the final number, then the prefix, a PAN, then the final check digit)



# Valid prefixes and lengths sourced from this article: https://www.x2q.net/post/bin-iin-lookup/ - There are likely other card networks I'm missing.
networks = { # Format is: "NETWORK_NAME": <possible_lengths>, <possible-prefixes>
    "VISA": [
        [13, 16, 19], 
        [4]
    ],
    "MASTERCARD": [
        [16], 
        [range(51, 56), range(2221, 2721)]
    ],
    "AMERICAN EXPRESS": [
        [15],
        [34, 37],
    ],
    "DISCOVER": [
        [range(16, 20)],
        [6011, range(644, 650), 65, range(622126, 622926)],
    ],
    "DINERS CLUB INTERNATIONAL": [
        [range(14, 20)],
        [36, range(300, 306), 3095, 38, 39],
    ],
    "JCB": [
        [range(16, 20)],
        [range(3528, 3590)],
    ],
    "UNIONPAY": [
        [range(12, 20)],
        [62, 81],
    ],
    "MAESTRO": [
        [range(12, 20)],
        [50, range(56, 70), 6304, 6759, 676770, 676774],
    ],
    "RUPAY": [
        [16],
        [60, 6521, 6522],
    ],
    "MIR": [
        [16],
        [range(2200, 2205)],
    ],
    "TROY": [
        [16],
        [9792]
    ],
}

# Length and prefix validation - Gets messy because of ranges as items in dict
def checkLength(network, length):
    possibleLengths, nothing = networks[network.upper()]

    return any(
        length in item if isinstance(item, range) else length == item
        for item in possibleLengths
    )

def checkPrefix(network, prefix):
    nothing, possiblePrefixes = networks[network.upper()]

    return any(
        prefix in item if isinstance(item, range) else prefix == item
        for item in possiblePrefixes
    )

def generateNumbers(network, length, prefix): # If no network or specific length is passed in, it will be picked randomly
    if network.upper() in networks:
        pass
    else:
        raise ValueError("Invalid card network selection")
    
    if checkLength(network, length):
        pass
    else:
        raise ValueError("Invalid length for selected card network")

    if checkPrefix(network, prefix):
        pass
    else:
        raise ValueError("Invalid prefix for selected card network")
    
    digits = str(prefix)

    for space in range(len(digits), length-1):
        digit = random.randint(0, 9)
        digits += str(digit)

    return digits


def pickRandom():
    network = random.choice(list(networks.keys()))

    prefix = random.choice(networks[network][1])
    possibleLengths, nothing = networks[network.upper()]
    
    length = any(
        length in item if isinstance(item, range) else length == item
        for item in possibleLengths
    )
    return network, prefix, length

def generateCard(network="", length=0, ):
    pass

print(pickRandom())