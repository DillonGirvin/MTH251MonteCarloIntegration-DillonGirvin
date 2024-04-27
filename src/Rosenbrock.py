# Libraries
import numpy
import numpy as np
import IntegralEstimates0

"""
Rosenbrock.py

This file is intended to solve the Rosenbrock Integral over the
bounds [-5, 5] for both x and y in two dimensions. The integral
is approximated using Monte Carlo Integration and then printed
to the console.

Note: The value computed by the program is incorrect, and the 
cause is unknown. The code does not function as expected. Additionally,
the number of samples used is high. If the program takes a while
to run, either wait or temporarily decrease the number of samples
on line
"""


# 2 Dimensional Uniform Distribution Class
class TwoDimUniform(object):
    """
    A two dimensional uniform distribution.
    """
    # Constructor
    def __init__(self, bounds=None):
        """
        Creates the two-dimensional uniform distribution over
        the bounds given.
        :param bounds:
        """
        # Set the bounds of the object to the bounds given.
        self.bounds: numpy.ndarray = np.array(bounds)

    # Random Variables
    def rvs(self, numPoints: int):
        """
        Creates an array of random variables within the
        uniform distribution.
        :param numPoints: The number of random variables to generate.
        :return: An array containing the random variables from
        the distribution.
        """
        # Create the random variables array
        randomVariables: numpy.ndarray = np.empty((len(self.bounds), numPoints))

        # For every point within the bounds
        for dimension in np.arange(len(self.bounds)):
            # Create and store an array of random uniformly chosen variables
            randomVariables[dimension]: np.ndarray = np.random.uniform(
                low=self.bounds[dimension][0],
                high=self.bounds[dimension][1],
                size=numPoints)

        # Return the transpose of the created array
        return randomVariables.T

    # Probability Density Function
    def pdf(self, randomVariables: np.ndarray):
        """
        The probability density function for the uniform
        distribution.
        :param randomVariables: An array of random variables
        to evaluate the probabilities of.
        :return: An array of probabilities corresponding to the
        random variables given.
        """
        # Determine how many variables can be chosen within the bounds
        numPossibleVariables = np.prod([self.bounds[:, 1] - self.bounds[:, 0]])

        # Return the array of probabilities for each variable
        return np.ones(randomVariables.shape[0]) / numPossibleVariables


def rosenbrockFunction(x1: float, x2: float):
    """
    The Rosenbrock Function as given in the MyCourses project
    specification.
    :param x1: The first variable for the function.
    :param x2: The second variable for the function.
    :return: The Rosenbrock Function evaluated at the x1 and x2 given.
    """
    return - (np.array(np.power((1. - x1), 2) + 100. * np.power((x2 - x1 ** 2), 2), dtype=float))


def main():
    """
    Creates a two-dimensional uniform distribution, and then uses
    Monte Carlo Integration to approximate the Rosenbrock Integral
    :return: None
    """
    # Create 2-Dimensional Uniform Distribution
    uniformDistribution = TwoDimUniform(bounds=[[-5, 5], [-5, 5]])

    mean, error = IntegralEstimates0.oneDimensionalIntegration(lambda x: rosenbrockFunction(*x.T), uniformDistribution,
                                                               100000000)

    # TODO - Determine why the output contains the incorrect mean and
    #  standard deviation
    print("Mean: " + str(mean) + "\tError: " + str(error))


if __name__ == '__main__':
    main()
