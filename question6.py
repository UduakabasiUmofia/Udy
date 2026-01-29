# question 6
def distributionAnalysis(numbers):
    result = {}
    totalCount = len(numbers)

    # remove duplicates and sort
    uniqueNumbers = sorted(set(numbers))

    for key in uniqueNumbers:
        countLessOrEqual = 0

        # count numbers <= key
        for num in numbers:
            if num <= key:
                countLessOrEqual += 1

        # convert to percentage
        percentage = (countLessOrEqual / totalCount) * 100
        result[key] = percentage

    return result


if __name__ == "__main__":
    sampleNumbers = [3, 1, 2, 3, 4, 2]
    print(distributionAnalysis(sampleNumbers))
