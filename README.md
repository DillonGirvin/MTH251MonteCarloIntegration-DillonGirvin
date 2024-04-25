# MTH 251 Probability and Statistics Final Project: Monte Carlo Integration
**Authors:** Alden Dimarco, Dillon Girvin

## Overview
This project utilizes Monte Carlo integration to solve the Rosenbrock integral over the interval \([-5,5]^2\). The Rosenbrock integral is defined as:

$$
\int \exp\left( -(1-x_1)^2 + 100(x_2 - x_1^2)^2 \right) \, dx_1 \, dx_2
$$



## Project Specifications
### Integral Estimates 0: Uniform, 1d
Using N = 10<sup>3</sup> evaluations, estimate the following integrals (both value and accuracy), using a uniform distribution:
1. On [-10, 10], f(x) = 1. Discuss your error estimate.
2. On [-1, 1], f(x) = P<sub><i>l</i></sub>(x)<sup>2</sup> for \(<i>l</i> = 0, 1, 2, 3, 4, 5\). The function P<sub><i>l</i></sub>(x) can be produced in Python with `scipy.special.eval_legendre(l, x)`.
3. On [-10, 10], f(x) is the standard normal PDF with mean 0 and variance 1.
4. On [-10, 10], f(x) is a weighted sum of two normal distributions p<sub>1</sub>(x) and p<sub>2</sub>(x) with means -3 and 3 and standard deviations 1 and 3 respectively, using

$$
f(x) = 0.7p_1(x) + 0.3p_2(x).
$$

### Integral Estimates 1: Gaussian, 1d
Using N = 10<sup>3</sup> evaluations, repeat parts (a,c,d) above (the standard normal PDF) but use a sampling distribution p<sub>s</sub>(x) which is the (appropriately truncated) standard normal distribution. Discuss how the uncertainty estimate in this section compares with the uncertainty in the previous section.

## Extra Credit Opportunities
- **Extra Credit 0:** Repeat the project using a (truncated?) normal distribution for the sampling distribution, with chosen mean and covariance to improve sampling efficiency. Explain the parameters selected for the sampling distribution and why.
- **Extra Credit 1:** Perform specific integrals by Monte Carlo integration to a relative accuracy of 10<sup>-2</sup>, carefully explaining the adopted sampling distributions and number of evaluations. The specific integrals to evaluate are within the project specifications in MyCourses.

## Files Included
- **IntegralEstimates0.py:** Contains code for estimating integrals using a uniform distribution.
- **IntegralEstimates1.py:** Contains code for estimating integrals using a Gaussian distribution.
- **Rosenbrock.py:** Contains code for solving the Rosenbrock integral over the interval [-5,5]^2.
- **ExtraCredit0.py:** (Possible file) Contains code for extra credit task 0, using a truncated normal distribution for improved sampling efficiency.
- **ExtraCredit1.py:** (Possible file) Contains code for extra credit task 1, performing specific integrals with a relative accuracy of 10<sup>-2</sup>.
