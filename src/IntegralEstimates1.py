# Libraries
import numpy as np
import scipy.stats

"""
IntegralEstimates0.py

This file is intended for use to solve the second set of Getting Started questions.
View the ReadMe to see which questions are being solved by the program. Once 
questions are solved, the answers are printed to the console to be viewed by
the user.

Note: The code within this program is identical to IntegralEstimates0.py, except the
sampling distribution used is the normal distribution instead of the uniform distribution,
and the second problem is removed.

Author: Dillon Girvin
"""


def problem1Func(x: np.ndarray):
    """
    The function for problem 1: f(x) = 1

    :param x: An unused parameter that is required for use in the
    integration method
    :return: 1 for all x given.
    """
    return 1


def problem3Func(x: np.ndarray):
    """
    The function for problem 3: The standard normal distribution
    with a mean of 0 and a variance of 1.

    :param x: The x value to evaluate the standard normal distribution at
    :return: The standard normal distribution at the given x value.
    """
    normal = scipy.stats.truncnorm(-10, 10, loc=0, scale=1)
    return normal.pdf(x)


def problem4Func(x: np.ndarray):
    """
    The function for problem 4: A weighted sum of 2 normal distributions.
    0.7p1(x) + 0.3p2(x)
    where p1 and p2 are the normal distribution with means of -3 and 3 and
    standard deviations of 1 and 3 respectively.
    :param x: The x value to evaluate the function at.
    :return: The value of the function at the given x.
    """
    normal1 = scipy.stats.truncnorm(-10, 10, loc=-3, scale=1)
    normal2 = scipy.stats.truncnorm(-10, 10, loc=3, scale=3)

    return 0.7 * normal1.pdf(x) + 0.3 * normal2.pdf(x)


# One dimensional example
def oneDimensionalIntegration(functionName, distribution, numPoints):
    """
    A function that approximates the given function using Monte carlo
    integration with 'numPoints' random variables from the provided
    sampling distribution.

    :param functionName: The name of the function to use
    :param distribution: The sampling distribution to use
    :param numPoints: The number of samples to use
    :return:
    mean: The mean of the function (the approximate value of
    the integral)
    error: The error of the function
    """
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
    """
    Uses Monte Carlo integration to evaluate several functions
    using a Normal sampling distribution.
    :return: None
    """
    # Create Distributions
    normalDistrib1 = scipy.stats.truncnorm(-10, 10, loc=0, scale=1)  # Normal Distribution from -10 to 10.

    # Number of points to use for the distributions
    numPoints: int = 10 ** 3

    # Create lists to hold mean and error
    means: list = []
    errors: list = []

    # Get the mean and error for 1
    tempMean, tempError = oneDimensionalIntegration(problem1Func, normalDistrib1, numPoints)

    # Add the mean and error to the list
    means.append(tempMean)
    errors.append(tempError)

    # Get the mean and error for 3
    tempMean, tempError = oneDimensionalIntegration(problem3Func, normalDistrib1, numPoints)

    # Add the means and error to the list
    means.append(tempMean)
    errors.append(tempError)

    # Get the mean and error for 4
    tempMean, tempError = oneDimensionalIntegration(problem4Func, normalDistrib1, numPoints)

    # Add the means and error to the list
    means.append(tempMean)
    errors.append(tempError)

    # Display results
    for i in range(len(means)):
        print("Problem " + str(i + 1) + ":\nMean: " + str(means[i]) + "\tError: " + str(errors[i]))


if __name__ == '__main__':
    main()
