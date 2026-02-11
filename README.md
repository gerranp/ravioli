# **RaVIOLi** - <u>Ra</u>ndom <u>V</u>ariable <u>I</u>nequalities and <u>O</u>perations <u>Li</u>brary

Manipulations and calculation of random variables.

## Tutorial

In this tutorial we will see how to use `ravioli` to complete calculations on statistical distributions. Due to the scope of the library, we will give a specific example using the Normal distribution and the `Normal` class.

We recommend the following for some background information on random variables: <https://en.m.wikipedia.org/wiki/Random_variable>.

For specific information on the Normal distribution included in this tutorial, we recommend the following: <https://en.m.wikipedia.org/wiki/Normal_distribution>.

Given two normal distributions $X$ and $Y$ defined as such:

$$X \sim Normal(5,2)$$
$$Y \sim Normal(10,2)$$

We will first perform operations to transform the distribution, before performing some probability calculations.

To begin, we will import the necessary module and define our random variables:

```python
import ravioli
X = ravioli.Normal(mean=5,variance=2)
Y = ravioli.Normal(mean=10,variance=4)
```
To check our variable has been set up correctly, we can call the `parameters` function to get a representation of our random variable:

```python
print(X.parameters)
```

This will return:

```python
'Normal(5,2)'
```

The commands `mean`, `variance` and `standard_deviation` can also be called to acheive the same effect:

```python
print(Y.mean(), Y.variance(), Y.standard_deviation())
```
```python
(10, 4, 2)
```

We can then use `ravioli` to perform manipulations on a random variable. For example, to create a random variable $Z$ which is equivalent to $X + 3$ we can use the following:

```python
Z = X.add(3)
```
Or, using operand overloading:
```python
Z = X + 3
```
In either case, calling the parameters of $Z$ will then produce the following:

```python
print(Z.parameters())
```
```python
'Normal(8,2)'
```

For normal distributions, we can also use this to add two random variables together. For example, to create a variable $A = X+Y$:

```python
A = X.add(Y)
print(A.parameters())
```

This would return:

```python
'Normal(15,6)'
```

Finally, `ravioli` can also be used to calculate probabilities. For example, to calculate the probability $P(X<6)$, we can use the following:

```python
print(X.less_than(6))
```

Alternatively, using operand overloading:

```python
P(X < 6)
```

This will return the result:

```python
0.6914625
```

## How to guides

### Creating a random variable

To create a random variable, you need to create a variable of the relevant class, ensuring you call the correct parameters. For example:

```python
import ravioli

normal_dist = ravioli.Normal(mean=3, variance=7)
poisson_dist = ravioli.Poisson(rate=2)
```
### Calculating parameters of random variables


### Performing operations on random variables

Regardless of the distribution class used, commands stay identical for performing operations. These include `add`, `subtract`, `multiply` and `divide`. For example:

```python
import ravioli

normal_dist = ravioli.Normal(mean=5, variance=7)

new_normal_dist = normal.dist.add(5)

new_normal_dist.parameters():
```
Would return:
```python
'Normal(10,7)'
```

### Calculating probabilities

Regardless of the distribution class used, commands stay identical for performing operations. These include `equal_to`, `less_than`, `less_than_euqal_to`, `greater_than`, `greater_than_equal_to`, `between` and `between_equal_to`. For example:

```python
import ravioli

geometric_dist = ravioli.Geometric(p=0.5)
print(geometric_dist.between_equal_to(lower=1, upper=3))
```
This would return:

```python
0.875
```

## Explanation

### A brief overview of statistical distributions

### 1. Normal Distribution

The normal distribution is a continuous probability distribution defined by two parameters: the mean ($\mu$) and the standard deviation ($\sigma$). The probability density function (PDF) is given by:

$$
f(x; \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2}
$$

#### Addition of Two Independent Normal Distributions
If $X \sim N(\mu_1, \sigma_1^2)$ and $Y \sim N(\mu_2, \sigma_2^2)$ are independent, then their sum is also normally distributed:

$$
X + Y \sim N(\mu_1 + \mu_2, \sigma_1^2 + \sigma_2^2)
$$

#### Addition of a Number
If $X \sim N(\mu, \sigma^2)$ and $c$ is a constant, then:

$$
X + c \sim N(\mu + c, \sigma^2)
$$

### 2. Binomial Distribution

The binomial distribution is a discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success ($p$). It has two parameters: the number of trials ($n$) and the probability of success ($p$). The probability mass function (PMF) is given by:

$$
P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}
$$
where $\binom{n}{k} = \frac{n!}{k!(n - k)!}$ is the binomial coefficient.


#### Addition of Two Independent Binomial Distributions
If $X \sim Binomial(n_1, p)$ and $Y \sim Binomial(n_2, p)$ are independent and have the *same probability of success* $p$, then their sum is also binomial:

$$
X + Y \sim Bin(n_1 + n_2, p)
$$
If the probabilities of success are different, it is not quite as straightforward and will likely lead to a distribution that is not itself binomail.

#### Addition of a Number
Adding a constant to a binomial random variable doesn't result in another standard distribution. The distribution of $X + c$ would simply be the probabilities of the original binomial distribution shifted by $c$.

#### Calculating Probabilities (e.g., $P(X < a)$)
$$
P(X < a) = \sum_{k=0}^{a - 1} \binom{n}{k} p^k (1 - p)^{n - k}
$$

### 3. Uniform Distribution

The continuous uniform distribution describes a situation where all values within a given interval $[a, b]$ are equally likely. Its probability density function (PDF) is:

$$
f(x; a, b) = \begin{cases}
    \frac{1}{b - a} & \text{for } a \le x \le b \\
    0               & \text{otherwise}
\end{cases}
$$

The discrete uniform distribution describes a situation where all values within a finite set are equally likely. If the set is $\{x_1, x_2, ..., x_n\}$, then $P(X = x_i) = \frac{1}{n}$ for all $i$.

#### Addition of a Number
If $X \sim Uniform(a, b)$ and $c$ is a constant, then:

$$
X + c \sim Uniform(a + c, b + c)
$$

#### Calculating Probabilities (e.g., $P(X < k)$ for continuous)
For a continuous uniform distribution $U(a, b)$:

$$
P(X < k) = \begin{cases}
    0               & \text{if } k \le a \\
    \frac{k - a}{b - a} & \text{if } a < k < b \\
    1               & \text{if } k \ge b
\end{cases}
$$

### 4. Poisson Distribution

The Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time with a known constant mean rate ($\lambda$). Its probability mass function (PMF) is:

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
$$


#### Addition of Two Independent Poisson Distributions
If $X \sim Poisson(\lambda_1)$ and $Y \sim Poisson(\lambda_2)$ are independent, then their sum is also Poisson:

$$
X + Y \sim Poisson(\lambda_1 + \lambda_2)
$$

#### Addition of a Number
Adding a constant to a Poisson random variable doesn't result in another standard distribution. The distribution of $X + c$ would simply be the probabilities of the original Poisson distribution shifted by $c$.

#### Calculating Probabilities (e.g., $P(X < a)$)
$$
P(X < a) = \sum_{k=0}^{a - 1} \frac{\lambda^k e^{-\lambda}}{k!}
$$

### 5. Exponential Distribution

The exponential distribution is a continuous probability distribution. Its probability density function (PDF) is:

$$
f(x; \lambda) = \lambda e^{-\lambda x} \quad \text{for } x \ge 0
$$


#### Addition of Two Independent Exponential Distributions
The sum of two independent exponential random variables with the same rate parameter $\lambda$ follows a Gamma distribution with shape parameter $k=2$ and rate parameter $\lambda$ (also known as an Erlang distribution). If the rate parameters are different, the distribution of the sum is more complex.

#### Addition of a Number
If $X \sim Exp(\lambda)$ and $c$ is a constant, then the distribution of $X + c$ is a shifted exponential distribution with the same rate parameter.

#### Calculating Probabilities (e.g., $P(X < a)$)
$$
P(X < a) = \int_{0}^{a} \lambda e^{-\lambda x} dx = 1 - e^{-\lambda a} \quad \text{for } a \ge 0
$$

### 6. Geometric Distribution

The geometric distribution is a discrete probability distribution that describes the number of trials needed for the first success in a sequence of independent Bernoulli trials, each with the same probability of success ($p$). There are two common parameterizations:
    * The number of failures before the first success. The PMF is $P(X = k) = (1 - p)^k p$, for $k = 0, 1, 2, ...$
    * The number of trials until the first success (including the successful trial). The PMF is $P(X = k) = (1 - p)^{k - 1} p$, for $k = 1, 2, 3, ...$

We will use the second parameterization here.

#### Addition of Two Independent Geometric Distributions
The sum of two independent geometric random variables with the same probability of success $p$ does not follow another standard distribution. It is related to the negative binomial distribution.

#### Addition of a Number
Adding a constant to a geometric random variable doesn't result in another standard distribution. The distribution of $X + c$ would simply be the probabilities of the original geometric distribution shifted by $c$.

#### Calculating Probabilities (e.g., $P(X < a)$)
$$
P(X < a) = \sum_{k=1}^{a - 1} (1 - p)^{k - 1} p
$$
This can also be calculated using the cumulative distribution function (CDF):
$$
F(k) = P(X \le k) = 1 - (1 - p)^k
$$
So, $P(X < a) = P(X \le a - 1) = 1 - (1 - p)^{a - 1}$ for $a \ge 2$, and $P(X < 1) = 0$.

## Reference

### List of Functionality

The following functions are written in `ravioli` for all distributions, along with their operand overloaded counterparts where applicable:

- `parameters` and simply calling the variable, i.e ```print(X)```
- `mean`
- `variance`
- `standard_deviation`
- `add` and `+` *
- `subtract` and `-` *
- `multiply` and `*`
- `divide` and `/`
- `equal_to` and `==` **
- `greater_than` and `>`
- `greater_than_equal_to` and `>=` ***
- `less_than` and `<`
- `less_than_equal_to` and `<=` ***
- `between`
- `between_equal_to` ***

\* this is between two distributions, or between a distribution and an integer/float, depending on the restrictions of each distribution. Where the output is not guaranteed to be of the same distribution type, it is not inlcuded.

\** this will simply return 0 in the case of normal, exponential and uniform due to the nature of continuous distributions.

\*** these will return the same result as their exclusive counterparts in the case of normal, exponential and uniform due to the nature of continuous distributions.

### Bibliography

The relavant pages on wikipedia prodvide a good overview of the details of each specific distribution.

For some additional reading, we recommend the following:

> Xie, Solomon. “Operations of Random Variables - Statistical Guess - Medium.” Medium, Statistical Guess, 13 Jan. 2019, medium.com/statistical-guess/operations-of-random-variables-9c5f17766ff1.

>Keizer, Jasmine. “Determine the Sum of Independent Random Variables (Poisson and Normal).” CFA, FRM, and Actuarial Exams Study Notes, AnalystPrep, 28 June 2019, analystprep.com/study-notes/actuarial-exams/soa/p-probability/univariate-random-variables/determine-the-sum-of-independent-random-variables-poisson-and-normal

For a deeper exploration into the topic, with mostly stretches beyond the scope of this library:

>Melvin Dale Springer. The Algebra of Random Variables. John Wiley & Sons, 1979.

We also wish to thank Dafydd Evans on his course content in the MA1500 module which helped us to develop the library.