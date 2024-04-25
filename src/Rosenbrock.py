# Libraries
import numpy
import numpy as np
import IntegralEstimates0

# TODO - Add pydocs

# 2 Dimensional Uniform Distribution Class
class TwoDimUniform(object):
    # Constructor
    def __init__(self, bounds=None):
        # Set the bounds of the object to the bounds given.
        self.bounds: numpy.ndarray = np.array(bounds)

    # Random Variables
    def rvs(self, numPoints: int):
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
        # Determine how many variables can be chosen within the bounds
        numPossibleVariables = np.prod([self.bounds[:, 1] - self.bounds[:, 0]])

        # Return the array of probabilities for each variable
        return np.ones(randomVariables.shape[0]) / numPossibleVariables


def rosenbrockFunction(x1: float, x2: float):
    return (1 - x1)**2 + 100 * (x2 - x1**2)**2


def main():
    # Create 2-Dimensional Uniform Distribution
    uniformDistribution = TwoDimUniform(bounds=[[-5, 5], [-5, 5]])

    mean, error = IntegralEstimates0.oneDimensionalIntegration(lambda x: rosenbrockFunction(*x.T), uniformDistribution,
                                                               100000000)

    print("Mean: " + str(mean) + "\tError: " + str(error))


if __name__ == '__main__':
    main()
