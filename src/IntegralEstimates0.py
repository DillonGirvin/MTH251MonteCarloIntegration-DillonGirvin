# Libraries
import numpy as np
import scipy.stats

"""
IntegralEstimates0.py

This file is intended for use to solve the first set of Getting Started questions.
View the ReadMe to see which questions are being solved by the program. Once 
questions are solved, the answers are printed to the console to be viewed by
the user.

Author: Dillon Girvin
"""


# TODO - Add pydoc for all methods


def problem1Func(x: np.ndarray):
    return 1


def problem2Func(x: np.ndarray):
    # Create L value
    lValue: int = 0

    returnVal = (scipy.special.eval_legendre(lValue, x)) ** 2

    def incrementLValue():
        nonlocal lValue
        lValue += 1
        return lValue

    return returnVal


def problem3Func(x: np.ndarray):
    normal = scipy.stats.truncnorm(-10, 10, loc=0, scale=1)
    return normal.pdf(x)


def problem4Func(x: np.ndarray):
    normal1 = scipy.stats.truncnorm(-10, 10, loc=-3, scale=1)
    normal2 = scipy.stats.truncnorm(-10, 10, loc=3, scale=3)

    return 0.7 * normal1.pdf(x) + 0.3 * normal2.pdf(x)


# One dimensional example
def oneDimensionalIntegration(functionName, distribution, numPoints):
    # Create Random Variables Array
    randomVars: np.ndarray = distribution.rvs(numPoints)

    # Create Probability Array for each Random Variable
    probabilities: np.ndarray = distribution.pdf(randomVars)

    # Find the mean of the random variables
    mean = np.mean(functionName(randomVars) / probabilities)

    # Find the error
    error = np.std(functionName(randomVars) / probabilities) / np.sqrt(numPoints)

    # Return the mean and error calculated
    return mean, error


def main():
    # Create Distributions
    uniformDistrib1 = scipy.stats.uniform(loc=-10, scale=20)  # Uniform Distribution from -10 to 10.
    uniformDistrib2 = scipy.stats.uniform(loc=-1, scale=2)  # Uniform Distribution from -1 to 1.

    # Number of points to use for the distributions
    numPoints: int = 10 ** 3

    # Create lists to hold mean and error
    means: list = []
    errors: list = []

    # Get the mean and error for 1
    tempMean, tempError = oneDimensionalIntegration(problem1Func, uniformDistrib1, numPoints)

    # Add the mean and error to the list
    means.append(tempMean)
    errors.append(tempError)

    # Get the mean and error for 2
    for i in range(0, 7):
        tempMean, tempError = oneDimensionalIntegration(problem2Func, uniformDistrib2, numPoints)

        # Add the means and error to the list
        means.append(tempMean)
        errors.append(tempError)

    # Get the mean and error for 3
    tempMean, tempError = oneDimensionalIntegration(problem3Func, uniformDistrib1, numPoints)

    # Add the means and error to the list
    means.append(tempMean)
    errors.append(tempError)

    # Get the mean and error for 4
    tempMean, tempError = oneDimensionalIntegration(problem4Func, uniformDistrib1, numPoints)

    # Add the means and error to the list
    means.append(tempMean)
    errors.append(tempError)

    # Display results
    for i in range(len(means)):
        if i > 0 and i < 8:
            print("Problem 2-" + str(i - 1) + ":\nMean: " + str(means[i]) + "\tError: " + str(errors[i]))
        elif i == 0:
            print("Problem " + str(i + 1) + ":\nMean: " + str(means[i]) + "\tError: " + str(errors[i]))
        else:
            print("Problem " + str(i - 6) + ":\nMean: " + str(means[i]) + "\tError: " + str(errors[i]))


if __name__ == '__main__':
    main()
