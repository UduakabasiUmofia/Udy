# question 5
import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # Validate type (must be integers)
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Invalid input: both radii must be positive integers."

    # Validate positive
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Invalid input: both radii must be positive integers."

    areaOfCircle1 = math.pi * (radiusOfCircle1 ** 2)
    areaOfCircle2 = math.pi * (radiusOfCircle2 ** 2)

    largerArea = max(areaOfCircle1, areaOfCircle2)
    smallerArea = min(areaOfCircle1, areaOfCircle2)

    coveragePercent = (smallerArea / largerArea) * 100

    return coveragePercent


# Example tests
print(circleAreaCoverage(3, 5))
print(circleAreaCoverage(-2, 4))
print(circleAreaCoverage(3.5, 2))
