# QUESTION 2


def stringInfo(words): # function
    result = {}

    # Loop through each word in the list
    for word in words:
        lengthOfWord = len(word)

        # Check if length is even or odd
        if lengthOfWord % 2 == 0:
            parityType = "even"
        else:
            parityType = "odd"

        # Store nested dictionary
        result[word] = {
            "length": lengthOfWord,
            "parity": parityType
        }

    return result


# Example test for running sake
sampleWords = ["data", "science"]
print(stringInfo(sampleWords))
