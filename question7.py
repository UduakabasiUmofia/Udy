# question 7
def convertTime(secondsSinceMidnight):
    # Validate input
    if not isinstance(secondsSinceMidnight, int) or secondsSinceMidnight < 0:
        return "Invalid input: must be a non-negative integer."

    hours = secondsSinceMidnight // 3600
    remainingSeconds = secondsSinceMidnight % 3600

    minutes = remainingSeconds // 60
    seconds = remainingSeconds % 60

    # Determine AM or PM
    if hours < 12:
        period = "AM"
    else:
        period = "PM"

    # Convert to 12-hour format
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours = hours - 12

    return f"{hours} {minutes} {seconds} {period}"


if __name__ == "__main__":
    print(convertTime(19067))
    print(convertTime(-5))
